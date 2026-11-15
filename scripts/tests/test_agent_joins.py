import os
import shlex
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

    def run_script(self, *args, session_id, fork_name=None, stdin='', extra_env=None):
        env = {key: value for key, value in os.environ.items()
               if key not in ('AGENT_FORK_NAME', 'CLAUDECODE', 'CLAUDE_CODE_SESSION_ID',
                              'HERDR_SESSION', 'TMUX')}
        env.update(CLAUDECODE='1', CLAUDE_CODE_SESSION_ID=session_id, **(extra_env or {}))
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

    def test_spawn_records_the_session_id_it_starts_the_fork_with(self):
        bin_dir = Path(self.temp.name) / 'bin'
        bin_dir.mkdir()
        calls = Path(self.temp.name) / 'tmux-args'
        fake_tmux = bin_dir / 'tmux'
        fake_tmux.write_text(f'#!/bin/sh\nprintf "%s\\n" "$@" > {shlex.quote(str(calls))}\n')
        fake_tmux.chmod(0o755)
        result = self.run_script(
            'spawn', 'Another topic', session_id='main-id', stdin='A brief.\n',
            extra_env={'TMUX': '1', 'PATH': f'{bin_dir}:{os.environ["PATH"]}'})
        self.assertEqual(result.returncode, 0, result.stderr)
        rows = [line.split('\t') for line in
                (self.state / 'forks.tsv').read_text().splitlines()]
        child = next(row for row in rows if row[0] == 'Claude-2')
        self.assertEqual(child[1], 'Claude')
        fork_command = shlex.split(calls.read_text().splitlines()[-1])
        session_flag = fork_command.index('--session-id')
        self.assertEqual(fork_command[session_flag + 1], child[2])
        self.assertRegex(child[2], r'^[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}$')

    def test_main_session_cannot_yield(self):
        result = self.run_script('yield', session_id='main-id', stdin='A note.\n')
        self.assertEqual(result.returncode, 1)
        self.assertIn('not a fork opened by spawn', result.stderr)


if __name__ == '__main__':
    unittest.main()
