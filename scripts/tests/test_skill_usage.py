import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / 'skills/engineering/workflow/maintain-skills/scripts/skill-usage.sh'


def write_jsonl(path, records):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(''.join(json.dumps(record) + '\n' for record in records))


class SkillUsageTests(unittest.TestCase):
    """Runs skill-usage.sh against a fake transcript tree under a fake HOME."""

    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.base = Path(temp.name).resolve()
        self.home = self.base / 'home'
        self.skills = self.base / 'skills'
        for name in ('alpha', 'beta', 'gamma', 'unused'):
            (self.skills / 'category' / name).mkdir(parents=True)
            (self.skills / 'category' / name / 'SKILL.md').write_text('test\n')
        self.work = str(self.base / 'work')
        self.excluded = str(self.base / 'excluded')

    def run_script(self, *args):
        env = {key: value for key, value in os.environ.items()
               if key not in ('CLAUDE_TRANSCRIPTS', 'CODEX_TRANSCRIPTS')}
        result = subprocess.run(
            ['bash', str(SCRIPT), *args, str(self.skills)],
            capture_output=True, text=True, env={**env, 'HOME': str(self.home)},
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        rows = [line.split() for line in result.stdout.splitlines()]
        self.assertEqual(rows[0], ['skill', 'invoked', 'read', 'last'])
        return {row[0]: row[1:] for row in rows[1:]}

    def add_claude_session(self, name, cwd, date):
        def record(kind, content):
            return {'type': kind, 'cwd': cwd, 'timestamp': f'{date}T10:00:00Z',
                    'message': {'content': content}}
        write_jsonl(self.home / '.claude/projects/-work' / f'{name}.jsonl', [
            record('user', '<command-name>/alpha</command-name>'),
            record('assistant', [{'type': 'tool_use', 'name': 'Skill',
                                  'input': {'skill': 'plugin:beta'}}]),
            record('assistant', [{'type': 'tool_use', 'name': 'Read',
                                  'input': {'file_path': '/x/gamma/SKILL.md'}}]),
        ])

    def add_codex_session(self, name, cwd, date):
        stamp = f'{date}T10:00:00Z'
        write_jsonl(self.home / '.codex/sessions/2026/11/09' / f'{name}.jsonl', [
            {'type': 'session_meta', 'timestamp': stamp, 'payload': {'cwd': cwd}},
            {'type': 'response_item', 'timestamp': stamp, 'payload': {
                'type': 'message', 'role': 'user',
                'content': [{'type': 'input_text', 'text': '<skill>\n<name>beta</name>'}]}},
            {'type': 'response_item', 'timestamp': stamp, 'payload': {
                'type': 'custom_tool_call', 'name': 'exec',
                'input': 'exec_command({cmd:"cat /x/alpha/SKILL.md"})'}},
        ])

    def test_counts_invocations_and_reads_per_session(self):
        self.add_claude_session('claude-1', self.work, '2026-11-01')
        self.add_claude_session('claude-2', self.work, '2026-11-03')
        self.add_codex_session('codex-1', self.work, '2026-11-05')
        self.assertEqual(self.run_script(), {
            'alpha': ['2', '1', '2026-11-05'],
            'beta': ['3', '0', '2026-11-05'],
            'gamma': ['0', '2', '2026-11-03'],
            'unused': ['0', '0', 'never'],
        })

    def test_since_and_exclude_cwd_filter_sessions(self):
        self.add_claude_session('old', self.work, '2026-10-01')
        self.add_claude_session('excluded', self.excluded, '2026-11-02')
        self.add_codex_session('codex-excluded', self.excluded + '/sub', '2026-11-05')
        self.add_codex_session('codex-kept', self.work, '2026-11-04')
        usage = self.run_script('--since', '2026-10-15', '--exclude-cwd', self.excluded)
        self.assertEqual(usage['alpha'], ['0', '1', '2026-11-04'])
        self.assertEqual(usage['beta'], ['1', '0', '2026-11-04'])
        self.assertEqual(usage['gamma'], ['0', '0', 'never'])

    def test_runs_without_codex_transcripts(self):
        self.add_claude_session('claude-1', self.work, '2026-11-01')
        self.assertEqual(self.run_script()['alpha'], ['1', '0', '2026-11-01'])


if __name__ == '__main__':
    unittest.main()
