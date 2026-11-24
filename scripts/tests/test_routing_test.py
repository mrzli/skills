import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / 'skills/engineering/workflow/maintain-skills/scripts/routing-test.sh'

CLAUDE_INIT = {'type': 'system', 'subtype': 'init', 'skills': ['alpha', 'plugin:beta']}
CLAUDE_TOOL_USE = {'type': 'assistant', 'message': {'content': [
    {'type': 'tool_use', 'name': 'Skill', 'input': {'skill': 'alpha'}},
]}}
CLAUDE_INJECTED = {'type': 'user', 'message': {'content': [
    {'type': 'text', 'text': '<skill><name>gamma</name>body</skill>'},
]}}
CODEX_ITEM = {'type': 'item.completed', 'item': {
    'type': 'command_execution', 'command': 'cat /x/some-skill/SKILL.md'}}


class RoutingTestTests(unittest.TestCase):
    """Runs routing-test.sh with fake claude and codex executables that print fixtures."""

    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.base = Path(temp.name).resolve()
        self.project = self.base / 'project'
        self.project.mkdir()
        self.bin = self.base / 'bin'
        self.bin.mkdir()
        self.args_file = self.base / 'args'

    def fake(self, name, records):
        fixture = self.base / f'{name}.jsonl'
        fixture.write_text(''.join(json.dumps(r) + '\n' for r in records))
        exe = self.bin / name
        exe.write_text(f'#!/usr/bin/env bash\nprintf "%s\\n" "$@" >"{self.args_file}"\ncat "{fixture}"\n')
        exe.chmod(0o755)

    def run_script(self, agent, *expected):
        cases_file = self.base / 'cases.tsv'
        cases_file.write_text(''.join(
            f'{self.project}\t{e}\trequest {i}\n' for i, e in enumerate(expected)))
        env = {k: v for k, v in os.environ.items() if k != 'ANTHROPIC_API_KEY'}
        env['PATH'] = f'{self.bin}:{env["PATH"]}'
        env['TMPDIR'] = str(self.base)
        result = subprocess.run(['bash', str(SCRIPT), '--agent', agent, str(cases_file)],
                                capture_output=True, text=True, env=env)
        self.assertEqual(result.returncode, 0, result.stderr)
        rows = [line.split() for line in result.stdout.splitlines()]
        return [row for row in rows if row and row[0].isdigit()]

    def test_claude_verdicts(self):
        self.fake('claude', [CLAUDE_INIT, CLAUDE_TOOL_USE, CLAUDE_INJECTED])
        rows = self.run_script('claude', 'alpha', 'beta', 'none', '!gamma', 'delta', 'beta,alpha')
        self.assertEqual([(r[1], r[2], r[3]) for r in rows], [
            ('alpha', 'alpha,gamma', 'pass'),
            ('beta', 'alpha,gamma', 'missed'),
            ('none', 'alpha,gamma', 'extra'),
            ('!gamma', 'alpha,gamma', 'extra'),
            ('delta', 'alpha,gamma', 'absent'),
            ('beta,alpha', 'alpha,gamma', 'pass'),
        ])

    def test_claude_skill_file_read(self):
        self.fake('claude', [CLAUDE_INIT, {'type': 'assistant', 'message': {'content': [
            {'type': 'tool_use', 'name': 'Read', 'input': {'file_path': '/x/alpha/SKILL.md'}},
        ]}}])
        rows = self.run_script('claude', 'alpha')
        self.assertEqual([(r[2], r[3]) for r in rows], [('alpha', 'pass')])

    def test_codex_skill_path_in_other_item(self):
        self.fake('codex', [{'type': 'item.completed', 'item': {
            'type': 'file_read', 'path': '/x/some-skill/SKILL.md'}}])
        rows = self.run_script('codex', 'some-skill')
        self.assertEqual([(r[2], r[3]) for r in rows], [('some-skill', 'pass')])

    def test_claude_loading_nothing(self):
        self.fake('claude', [CLAUDE_INIT])
        rows = self.run_script('claude', 'none', 'alpha')
        self.assertEqual([(r[2], r[3]) for r in rows], [('-', 'pass'), ('-', 'missed')])

    def test_claude_passes_disallowed_tools_as_separate_arguments(self):
        self.fake('claude', [CLAUDE_INIT])
        self.run_script('claude', 'none')
        args = self.args_file.read_text().splitlines()
        start = args.index('--disallowedTools')
        self.assertEqual(args[start + 1:start + 4], ['Edit', 'Write', 'NotebookEdit'])

    def test_codex_skill_paths(self):
        self.fake('codex', [CODEX_ITEM])
        rows = self.run_script('codex', 'some-skill', 'other', 'none')
        self.assertEqual([(r[2], r[3]) for r in rows], [
            ('some-skill', 'pass'), ('some-skill', 'missed'), ('some-skill', 'extra')])


if __name__ == '__main__':
    unittest.main()
