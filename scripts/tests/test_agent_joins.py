import os
import subprocess
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[2] / 'skills/shared/scripts/agent-joins.sh'
CREATED = '2026-11-15T00:00:00Z'


class AgentJoinsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name)
        subprocess.run(['git', 'init', '-q'], cwd=self.repo, check=True)
        self.state = self.repo / '.git/agent-joins'
        self.state.mkdir()
        rows = [
            ['Claude', '-', 'main-id', '-', CREATED, '0', '-'],
            ['Claude-1', 'Claude', 'fork-id', 'Topic', CREATED, '0', '-'],
        ]
        (self.state / 'forks.tsv').write_text(
            ''.join('\t'.join(row) + '\n' for row in rows))

    def run_script(self, *args, session_id, fork_name=None, stdin=''):
        env = {key: value for key, value in os.environ.items()
               if key not in ('AGENT_FORK_NAME', 'CLAUDECODE', 'CLAUDE_CODE_SESSION_ID')}
        env.update(CLAUDECODE='1', CLAUDE_CODE_SESSION_ID=session_id)
        if fork_name is not None:
            env['AGENT_FORK_NAME'] = fork_name
        return subprocess.run(['bash', str(SCRIPT), *args], cwd=self.repo,
                              input=stdin, capture_output=True, text=True, env=env)

    def test_restarted_fork_yields_by_session_id(self):
        result = self.run_script('yield', session_id='fork-id', stdin='A note.\n')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('note of Claude-1', result.stdout)
        self.assertIn('A note.', (self.state / 'notes/Claude-1.md').read_text())

    def test_fork_name_takes_precedence_over_session_id(self):
        result = self.run_script('yield', session_id='main-id', fork_name='Claude-1',
                                 stdin='A note.\n')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('note of Claude-1', result.stdout)

    def test_main_session_cannot_yield(self):
        result = self.run_script('yield', session_id='main-id', stdin='A note.\n')
        self.assertEqual(result.returncode, 1)
        self.assertIn('not a fork opened by spawn', result.stderr)


if __name__ == '__main__':
    unittest.main()
