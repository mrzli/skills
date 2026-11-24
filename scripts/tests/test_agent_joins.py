import os
import shlex
import subprocess
import tempfile
import unittest
from datetime import datetime, timezone
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

    def test_fork_without_a_recorded_id_records_it_on_its_first_run(self):
        rows = (self.state / 'forks.tsv').read_text().replace('fork-id', '-')
        (self.state / 'forks.tsv').write_text(rows)
        result = self.run_script('yield', session_id='fork-id', fork_name='Claude-1',
                                 stdin='A note.\n')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('\tfork-id\t', (self.state / 'forks.tsv').read_text())
        result = self.run_script('yield', session_id='fork-id', stdin='Another note.\n')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('note of Claude-1', result.stdout)

    def test_main_session_cannot_yield(self):
        result = self.run_script('yield', session_id='main-id', stdin='A note.\n')
        self.assertEqual(result.returncode, 1)
        self.assertIn('not a fork opened by spawn', result.stderr)

    def add_forks(self, *rows):
        with (self.state / 'forks.tsv').open('a') as file:
            file.write(''.join('\t'.join(row) + '\n' for row in rows))

    def test_collect_reports_new_then_changed_notes(self):
        self.add_forks(['Claude-1-1', 'Claude-1', 'grand-id', 'Deep', CREATED, '0', '-'])
        self.run_script('yield', session_id='fork-id', stdin='First.\n')
        self.run_script('yield', session_id='grand-id', stdin='Deep first.\n')
        result = self.run_script('collect', session_id='main-id')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('=== Claude-1: new note, version 1 ===', result.stdout)
        self.assertIn('=== Claude-1-1: new note, version 1, via Claude-1 ===', result.stdout)
        self.run_script('yield', session_id='fork-id', stdin='Second.\n')
        result = self.run_script('collect', session_id='main-id')
        self.assertIn('=== Claude-1: changed note, version 2 ===', result.stdout)
        self.assertNotIn('=== Claude-1-1:', result.stdout)

    def test_collect_names_the_forks_between_a_note_and_the_collector(self):
        self.add_forks(['Claude-1-1', 'Claude-1', 'grand-id', 'Deep', CREATED, '0', '-'],
                       ['Claude-1-1-1', 'Claude-1-1', 'great-id', '-', CREATED, '0', '-'])
        self.run_script('yield', session_id='great-id', stdin='Deepest.\n')
        result = self.run_script('collect', session_id='main-id')
        self.assertIn('=== Claude-1-1-1: new note, version 1, via Claude-1, Claude-1-1 ===',
                      result.stdout)
        result = self.run_script('collect', session_id='fork-id')
        self.assertIn('=== Claude-1-1-1: new note, version 1, via Claude-1-1 ===',
                      result.stdout)

    def test_note_is_deleted_once_every_session_above_has_collected_it(self):
        self.add_forks(['Claude-1-1', 'Claude-1', 'grand-id', 'Deep', CREATED, '0', '-'])
        self.run_script('yield', session_id='fork-id', stdin='First.\n')
        self.run_script('yield', session_id='grand-id', stdin='Deep.\n')
        result = self.run_script('collect', session_id='main-id')
        self.assertIn('Deleted the note of Claude-1: every session above it has collected it.',
                      result.stdout)
        self.assertFalse((self.state / 'notes/Claude-1.md').exists())
        self.assertIn('Kept the note of Claude-1-1: not yet collected by Claude-1.',
                      result.stdout)
        self.assertTrue((self.state / 'notes/Claude-1-1.md').exists())
        result = self.run_script('collect', session_id='fork-id')
        self.assertIn('=== Claude-1-1: new note, version 1 ===', result.stdout)
        self.assertIn('Deleted the note of Claude-1-1', result.stdout)
        self.assertFalse((self.state / 'notes/Claude-1-1.md').exists())

    def test_inactive_tree_is_listed_and_prune_deletes_it(self):
        old = '2020-06-15T12:00:00Z'
        (self.state / 'forks.tsv').write_text(
            '\t'.join(['Claude', '-', 'main-id', '-', old, '0', '-']) + '\n'
            + '\t'.join(['Claude-1', 'Claude', 'fork-id', 'Topic', old, '1', '-']) + '\n')
        (self.state / 'notes').mkdir()
        (self.state / 'briefs').mkdir()
        (self.state / 'notes/Claude-1.md').write_text('An old note.\n')
        (self.state / 'briefs/Claude-1.md').write_text('An old brief.\n')
        result = self.run_script('collect', session_id='')
        self.assertIn('Inactive since 2020-06-15: the tree of Claude (sessions: 2, '
                      'notes left: 1). Delete it with: prune Claude', result.stdout)
        result = self.run_script('prune', 'Claude-1', session_id='')
        self.assertEqual(result.returncode, 1)
        self.assertIn('Not the main session of a recorded tree: Claude-1', result.stderr)
        result = self.run_script('prune', 'Claude', session_id='')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('Deleted the tree of Claude.', result.stdout)
        self.assertEqual((self.state / 'forks.tsv').read_text(), '')
        self.assertFalse((self.state / 'notes/Claude-1.md').exists())
        self.assertFalse((self.state / 'briefs/Claude-1.md').exists())

    def test_recently_active_tree_is_not_listed_as_inactive(self):
        now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
        (self.state / 'forks.tsv').write_text(
            '\t'.join(['Claude', '-', 'main-id', '-', now, '0', '-']) + '\n')
        result = self.run_script('collect', session_id='')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn('Inactive', result.stdout)


if __name__ == '__main__':
    unittest.main()
