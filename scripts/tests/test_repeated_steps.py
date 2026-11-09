import json
import os
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / 'skills/engineering/workflow/improve-workflow/scripts/repeated-steps.py'
CHAIN = 'git add <arg> ; git commit -m <arg>'
FILTER = 'npm test ; tail -n <arg>'


def write_jsonl(path, records):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(''.join(json.dumps(record) + '\n' for record in records))


class RepeatedStepsTests(unittest.TestCase):
    """Runs repeated-steps.py against a fake transcript tree under a fake HOME."""

    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.base = Path(temp.name).resolve()
        self.home = self.base / 'home'
        self.project = self.base / 'work' / 'my_project'
        self.project.mkdir(parents=True)
        self.slug = re.sub(r'[^A-Za-z0-9]', '-', str(self.project))

    def run_script(self, *args):
        result = subprocess.run(
            [sys.executable, '-I', str(SCRIPT), str(self.project), *args],
            capture_output=True, text=True, env={**os.environ, 'HOME': str(self.home)},
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout

    def add_claude_session(self, path, commands, date='2026-11-01'):
        records = []
        for index, command in enumerate(commands):
            records.append({'type': 'assistant', 'timestamp': f'{date}T10:00:00Z', 'message': {
                'content': [{'type': 'tool_use', 'id': f't{index}', 'name': 'Bash',
                             'input': {'command': command}}]}})
            records.append({'type': 'user', 'timestamp': f'{date}T10:01:00Z', 'message': {
                'content': [{'type': 'tool_result', 'tool_use_id': f't{index}', 'content': ''}]}})
        write_jsonl(self.home / '.claude/projects' / path, records)

    def add_codex_session(self, name, cwd, commands, date='2026-11-02'):
        stamp = f'{date}T10:00:00Z'
        records = [{'type': 'session_meta', 'timestamp': stamp, 'payload': {'cwd': str(cwd)}}]
        for command in commands:
            records.append({'type': 'response_item', 'timestamp': stamp, 'payload': {
                'type': 'custom_tool_call', 'name': 'exec',
                'input': f'text(await tools.exec_command({{cmd:{json.dumps(command)}}}));'}})
        write_jsonl(self.home / '.codex/sessions/2026/11/02' / f'{name}.jsonl', records)

    def shape_line(self, output, shape):
        return next((line.split() for line in output.splitlines() if line.endswith(shape)), None)

    def test_counts_chains_across_project_folders_and_nested_files(self):
        commit = 'git add a.txt && git commit -m "Fix it"'
        self.add_claude_session(f'{self.slug}/s1.jsonl', [commit, 'ls', commit])
        self.add_claude_session(f'{self.slug}-claude-worktrees-x/sub/s2.jsonl', [commit])
        self.add_claude_session('-elsewhere/s3.jsonl', [commit] * 5)
        output = self.run_script()
        self.assertIn('4 commands in', output)
        self.assertIn('2026-11-01 to 2026-11-01', output)
        # times, sessions, minutes (one minute per command), kind
        self.assertEqual(self.shape_line(output, CHAIN)[:4], ['3', '2', '3.0', 'chain:'])

    def test_reads_codex_sessions_by_cwd(self):
        test = 'npm test | tail -n 5'
        self.add_codex_session('here', self.project, [test, test])
        self.add_codex_session('below', self.project / 'sub', [test])
        self.add_codex_session('elsewhere', self.base / 'other', [test] * 5)
        output = self.run_script()
        self.assertIn('3 commands in', output)
        self.assertEqual(self.shape_line(output, FILTER)[:4], ['3', '2', '0.0', 'filter:'])

    def test_since_drops_older_commands(self):
        commit = 'git add a.txt && git commit -m "Fix it"'
        self.add_claude_session(f'{self.slug}/s1.jsonl', [commit] * 3, date='2026-10-01')
        output = self.run_script('--since', '2026-10-15')
        self.assertIn('0 commands in', output)
        self.assertIsNone(self.shape_line(output, CHAIN))


if __name__ == '__main__':
    unittest.main()
