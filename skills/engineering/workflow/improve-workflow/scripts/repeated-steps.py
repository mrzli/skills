#!/usr/bin/env python3
"""Count shell steps that agents repeated by hand in one project.

Reads the Claude Code and Codex transcripts of the project, reduces each
command to its shape (names, paths and numbers replaced by placeholders), and
prints the shapes seen most often that are more than one project command:
chains of commands, loops, and output filters. Deciding which are worth a
script is left to the reader.

Usage: repeated-steps.py [PROJECT_DIR] [--since YYYY-MM-DD] [--top N]
"""

import argparse
import collections
import glob
import json
import os
import re
import shlex
from datetime import datetime

CLAUDE_PROJECTS = os.path.expanduser("~/.claude/projects")
CODEX_SESSIONS = os.path.expanduser("~/.codex/sessions")

# Commands that only read or report; a chain made only of these is a lookup.
LOOKUPS = {
    "cat", "ls", "head", "tail", "wc", "grep", "rg", "find", "sed", "awk",
    "echo", "pwd", "readlink", "stat", "file", "du", "which", "sort", "uniq",
    "cut", "tr", "diff", "true", "printf", "test", "[",
}
FILTERS = {"grep", "rg", "tail", "head", "sed", "awk", "cut", "sort", "uniq", "wc"}


def parse_time(value):
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (AttributeError, ValueError):
        return None


def claude_commands(project):
    """Yields (session, time, seconds, command) from Claude Code transcripts."""
    prefix = re.sub(r"[^A-Za-z0-9]", "-", project)
    for folder in glob.glob(os.path.join(CLAUDE_PROJECTS, glob.escape(prefix) + "*")):
        for path in glob.glob(os.path.join(folder, "**", "*.jsonl"), recursive=True):
            started, finished = {}, {}
            for line in open(path, errors="replace"):
                try:
                    record = json.loads(line)
                except ValueError:
                    continue
                content = (record.get("message") or {}).get("content")
                if not isinstance(content, list):
                    continue
                when = parse_time(record.get("timestamp"))
                for block in content:
                    if not isinstance(block, dict):
                        continue
                    if block.get("type") == "tool_use" and block.get("name") == "Bash":
                        command = (block.get("input") or {}).get("command")
                        if isinstance(command, str):
                            started[block.get("id")] = (when, command)
                    elif block.get("type") == "tool_result":
                        finished[block.get("tool_use_id")] = when
            for key, (when, command) in started.items():
                end = finished.get(key)
                seconds = (end - when).total_seconds() if when and end else 0.0
                yield path, when, max(seconds, 0.0), command


CODEX_COMMAND = re.compile(r'exec_command\(\{\s*cmd\s*:\s*("(?:\\.|[^"\\])*")')


def codex_commands(project):
    """Yields (session, time, seconds, command) from Codex transcripts."""
    for path in glob.glob(os.path.join(CODEX_SESSIONS, "**", "*.jsonl"), recursive=True):
        inside = False
        for line in open(path, errors="replace"):
            try:
                record = json.loads(line)
            except ValueError:
                continue
            payload = record.get("payload") or {}
            if record.get("type") == "session_meta":
                cwd = payload.get("cwd") or ""
                inside = cwd == project or cwd.startswith(project + "/")
                if not inside:
                    break
                continue
            if not inside or record.get("type") != "response_item":
                continue
            text = payload.get("input") or payload.get("arguments") or ""
            if not isinstance(text, str):
                continue
            for match in CODEX_COMMAND.finditer(text):
                try:
                    command = json.loads(match.group(1))
                except ValueError:
                    continue
                yield path, parse_time(record.get("timestamp")), 0.0, command


HEREDOC = re.compile(r"<<-?\s*['\"]?(\w+)['\"]?.*?\n.*?\n\s*\1\b", re.S)
SUBCOMMAND = re.compile(r"^[a-z][a-z-]*$")


def word_shape(word, position):
    if word.startswith("-"):
        return word.split("=", 1)[0]
    if "=" in word and position == 0:
        return word.split("=", 1)[0] + "=<v>"
    if position <= 2 and SUBCOMMAND.match(word):
        return word
    return "<arg>"


def step_shape(step):
    """The shape of one simple command, or None for an empty step."""
    step = step.strip()
    if not step:
        return None
    try:
        words = shlex.split(step, comments=False)
    except ValueError:
        words = step.split()
    # Settings before the program, such as QT_SCALE_FACTOR=2, keep their name.
    shaped = []
    while words and re.match(r"^[A-Za-z_][A-Za-z0-9_]*=", words[0]):
        shaped.append(words[0].split("=", 1)[0] + "=<v>")
        words = words[1:]
    if not words or not words[0]:
        return None
    program = words[0]
    if "/" in program and not program.startswith(("./", "bin/")):
        program = os.path.basename(program)
    shaped.append(program)
    position = 1
    for word in words[1:]:
        shape = word_shape(word, position)
        if shape == "<arg>" and shaped[-1] == "<arg>":
            continue
        shaped.append(shape)
        if not word.startswith("-"):
            position += 1
    return " ".join(shaped)


def split_steps(command):
    """Splits at &&, ||, ;, | and newlines outside quotes, keeping the joints."""
    pieces, current, quote, index = [], [], None, 0
    while index < len(command):
        char = command[index]
        if quote:
            if char == "\\" and quote == '"' and index + 1 < len(command):
                current.append(command[index:index + 2])
                index += 2
                continue
            if char == quote:
                quote = None
            current.append(char)
        elif char in "'\"":
            quote = char
            current.append(char)
        else:
            joint = next((j for j in ("&&", "||", ";", "\n", "|") if command.startswith(j, index)), None)
            if joint:
                pieces.extend(["".join(current), joint])
                current = []
                index += len(joint)
                continue
            current.append(char)
        index += 1
    pieces.append("".join(current))
    return pieces


def program_of(shape):
    """The program a step's shape runs, after any settings before it."""
    return next((w for w in shape.split() if not w.endswith("=<v>")), "")


def command_shape(command):
    """Returns (shape, steps, kind) for a whole command line."""
    command = HEREDOC.sub("<<heredoc", command)
    command = re.sub(r"\\\n", " ", command)
    loop = re.search(r"\b(for|while)\b.*?\bdo\b", command, re.S) is not None
    pieces = split_steps(command)
    steps, joints = [], []
    for index, piece in enumerate(pieces):
        if index % 2:
            joints.append(piece.strip() or ";")
            continue
        if re.match(r"\s*cd\b", piece) and index + 1 < len(pieces):
            continue
        shape = step_shape(piece)
        if shape is not None:
            steps.append(shape)
    if not steps:
        return None, [], ""
    filtered = any(j == "|" for j in joints) and program_of(steps[-1]) in FILTERS
    kind = "loop" if loop else "filter" if filtered else "chain" if len(steps) > 1 else "single"
    return " ; ".join(steps), steps, kind


def is_candidate(steps, kind):
    if kind == "single":
        return False
    programs = {program_of(s) for s in steps}
    if kind == "chain" and programs <= LOOKUPS:
        return False
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("project", nargs="?", default=os.getcwd())
    parser.add_argument("--since", help="only sessions on or after this date")
    parser.add_argument("--top", type=int, default=25)
    options = parser.parse_args()
    project = os.path.realpath(options.project)
    since = datetime.fromisoformat(options.since).date() if options.since else None

    counts = collections.Counter()
    sessions = collections.defaultdict(set)
    seconds = collections.Counter()
    kinds, examples = {}, {}
    runs = collections.Counter()
    run_sessions = collections.defaultdict(set)
    run_examples = {}
    total, first, last = 0, None, None
    for source in (claude_commands(project), codex_commands(project)):
        for session, when, spent, command in source:
            if since and when and when.date() < since:
                continue
            total += 1
            if when:
                first = min(first, when) if first else when
                last = max(last, when) if last else when
            shape, steps, kind = command_shape(command)
            useful = [s for s in steps if program_of(s) not in ("echo", "printf", "true", "set")]
            seen = set()
            for length in (2, 3, 4):
                for start in range(len(useful) - length + 1):
                    run = tuple(useful[start:start + length])
                    if run in seen or {program_of(r) for r in run} <= LOOKUPS:
                        continue
                    seen.add(run)
                    runs[run] += 1
                    run_sessions[run].add(session)
                    run_examples.setdefault(run, " ".join(command.split())[:160])
            if not shape or not is_candidate(steps, kind):
                continue
            counts[shape] += 1
            sessions[shape].add(session)
            seconds[shape] += spent
            kinds[shape] = kind
            examples.setdefault(shape, " ".join(command.split())[:160])

    span = f"{first:%Y-%m-%d} to {last:%Y-%m-%d}" if first else "no sessions"
    print(f"{total} commands in {project}, {span}.")
    print("Repeated chains, loops and output filters (times, sessions, minutes):\n")
    for shape, count in counts.most_common(options.top):
        if count < 3:
            break
        print(f"{count:5}  {len(sessions[shape]):3}  {seconds[shape] / 60:6.1f}  {kinds[shape]}: {shape}")
        print(f"{'':20}e.g. {examples[shape]}")
    # A run counts only where it is not just part of a longer run seen as often.
    print("\nRepeated runs of steps inside commands (times, sessions):\n")
    shown = 0
    for run, count in runs.most_common():
        if count < 3 or shown >= options.top:
            break
        longer = [r for r in runs if len(r) > len(run) and runs[r] == count
                  and any(r[i:i + len(run)] == run for i in range(len(r) - len(run) + 1))]
        if longer:
            continue
        shown += 1
        print(f"{count:5}  {len(run_sessions[run]):3}  " + " ; ".join(run))
        print(f"{'':12}e.g. {run_examples[run]}")


if __name__ == "__main__":
    main()
