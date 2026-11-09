import json
import os
import re
import subprocess
import tempfile
import time
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / 'skills/conversation/warmup/scripts/last-session.sh'


def write_jsonl(path, records, mtime):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(''.join(json.dumps(record) + '\n' for record in records))
    os.utime(path, (mtime, mtime))


class LastSessionTests(unittest.TestCase):
    """Runs last-session.sh against a fake transcript tree under a fake HOME."""

    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.base = Path(temp.name).resolve()
        self.home = self.base / 'home'
        self.project = self.base / 'work' / 'my_project x.y'
        self.project.mkdir(parents=True)
        self.claude = self.home / '.claude/projects' / re.sub(r'[^a-zA-Z0-9]', '-', str(self.project))
        self.now = int(time.time())
        self.codex = self.home / '.codex/sessions/2026/11/09'

    def run_script(self, *args):
        env = {key: value for key, value in os.environ.items()
               if key not in ('CLAUDE_TRANSCRIPTS', 'CODEX_TRANSCRIPTS')}
        return subprocess.run(
            ['bash', str(SCRIPT), *args, str(self.project)],
            capture_output=True, text=True, env={**env, 'HOME': str(self.home)},
        )

    def add_claude_session(self, name, mtime):
        write_jsonl(self.claude / f'{name}.jsonl', [
            {'type': 'user', 'isMeta': True, 'message': {'content': 'meta note'}},
            {'type': 'user', 'message': {'content': f'question in {name}'}},
            {'type': 'assistant', 'message': {'content': [
                {'type': 'text', 'text': f'answer in {name}'},
                {'type': 'tool_use', 'name': 'Bash', 'input': {'command': 'ls'}},
            ]}},
            {'type': 'user', 'message': {'content': [
                {'type': 'tool_result', 'tool_use_id': 'x', 'content': 'tool output'},
            ]}},
        ], mtime)

    def add_codex_session(self, name, cwd, mtime):
        write_jsonl(self.codex / f'{name}.jsonl', [
            {'type': 'session_meta', 'payload': {'cwd': str(cwd)}},
            {'type': 'response_item', 'payload': {
                'type': 'message', 'role': 'user',
                'content': [{'type': 'input_text', 'text': '<environment_context>x'}]}},
            {'type': 'response_item', 'payload': {
                'type': 'message', 'role': 'user',
                'content': [{'type': 'input_text', 'text': f'question in {name}'}]}},
            {'type': 'response_item', 'payload': {
                'type': 'message', 'role': 'assistant',
                'content': [{'type': 'output_text', 'text': f'answer in {name}'}]}},
        ], mtime)

    def test_prints_previous_claude_session_without_tools_or_meta(self):
        self.add_claude_session('older', self.now - 100)
        self.add_claude_session('current', self.now)
        result = self.run_script()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('older.jsonl', result.stdout)
        self.assertIn('USER:\nquestion in older', result.stdout)
        self.assertIn('ASSISTANT:\nanswer in older', result.stdout)
        self.assertNotIn('current', result.stdout)
        self.assertNotIn('meta note', result.stdout)
        self.assertNotIn('tool output', result.stdout)

    def test_finds_codex_session_by_cwd(self):
        self.add_claude_session('current', self.now)
        self.add_codex_session('codex-here', self.project, self.now - 100)
        self.add_codex_session('codex-elsewhere', self.base / 'other', self.now - 50)
        result = self.run_script()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(f"codex {self.codex / 'codex-here.jsonl'}", result.stdout)
        self.assertIn('USER:\nquestion in codex-here', result.stdout)
        self.assertIn('ASSISTANT:\nanswer in codex-here', result.stdout)
        self.assertNotIn('environment_context', result.stdout)
        self.assertNotIn('codex-elsewhere', result.stdout)

    def test_reports_missing_earlier_session(self):
        self.add_claude_session('current', self.now)
        result = self.run_script()
        self.assertEqual(result.returncode, 1)
        self.assertIn('No earlier session', result.stderr)


if __name__ == '__main__':
    unittest.main()
