import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / 'sync-skills.sh'


class SyncSkillsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.repo = self.base / 'repo'
        (self.repo / 'scripts').mkdir(parents=True)
        shutil.copy2(SCRIPT, self.repo / 'scripts/sync-skills.sh')
        self.add_skill('productivity', 'example')
        self.destinations = [self.repo / directory / 'skills'
                             for directory in ('.agents', '.claude')]

    def add_skill(self, category, name):
        directory = self.repo / 'skills' / category / name
        directory.mkdir(parents=True)
        (directory / 'SKILL.md').write_text('test\n')

    def sync(self, *args):
        return subprocess.run(
            ['bash', str(self.repo / 'scripts/sync-skills.sh'), *args],
            cwd=self.base, capture_output=True, text=True,
            env={**os.environ, 'HOME': str(self.home)},
        )

    @property
    def home(self):
        return self.base / 'home'

    @property
    def user_destinations(self):
        return [self.home / directory / 'skills' for directory in ('.agents', '.claude')]

    def test_rejects_unknown_arguments(self):
        for args in (['--users'], ['--user', '--user']):
            with self.subTest(args=args):
                result = self.sync(*args)
                self.assertEqual(result.returncode, 2)
                self.assertIn('Usage', result.stderr)

    def test_user_sync_links_absolute_and_removes_stale(self):
        result = self.sync('--user')
        self.assertEqual(result.returncode, 0, result.stderr)
        for directory in self.user_destinations:
            link = directory / 'example'
            self.assertEqual(os.readlink(link),
                             str(self.repo / 'skills/productivity/example'))
            (directory / 'unrelated').symlink_to(self.base / 'external')
            (directory / 'relative').symlink_to('../../skills/productivity/gone')
        for directory in self.destinations:
            self.assertFalse(directory.exists())
        repeat = self.sync('--user')
        self.assertEqual(repeat.returncode, 0, repeat.stderr)
        self.assertEqual(repeat.stdout, '')
        shutil.rmtree(self.repo / 'skills/productivity/example')
        self.add_skill('productivity', 'new')
        self.assertEqual(self.sync('--user').returncode, 0)
        for directory in self.user_destinations:
            self.assertFalse((directory / 'example').is_symlink())
            self.assertTrue((directory / 'new').is_symlink())
            self.assertTrue((directory / 'unrelated').is_symlink())
            self.assertTrue((directory / 'relative').is_symlink())

    def test_user_sync_refuses_unmanaged_skill_before_changes(self):
        other = self.base / 'other/example'
        other.mkdir(parents=True)
        self.user_destinations[1].mkdir(parents=True)
        (self.user_destinations[1] / 'example').symlink_to(other)
        result = self.sync('--user')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('does not manage', result.stderr)
        self.assertNotIn('broken link', result.stderr)
        self.assertFalse(self.user_destinations[0].exists())
        self.assertEqual((self.user_destinations[1] / 'example').resolve(), other)

    def test_user_sync_after_moved_clone_suggests_removing_broken_links(self):
        self.assertEqual(self.sync('--user').returncode, 0)
        moved = self.base / 'moved'
        self.repo.rename(moved)
        self.repo = moved
        result = self.sync('--user')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('broken link', result.stderr)
        command = next(line.strip() for line in result.stderr.splitlines()
                       if line.strip().startswith('find '))
        subprocess.run(command, shell=True, check=True)
        result = self.sync('--user')
        self.assertEqual(result.returncode, 0, result.stderr)
        for directory in self.user_destinations:
            self.assertEqual((directory / 'example').resolve(),
                             moved / 'skills/productivity/example')

    def test_user_sync_follows_symlinked_destination(self):
        dotfiles = self.base / 'dotfiles/claude'
        dotfiles.mkdir(parents=True)
        self.home.mkdir()
        (self.home / '.claude').symlink_to(dotfiles, target_is_directory=True)
        result = self.sync('--user')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((dotfiles / 'skills/example').is_symlink())

    def test_sync_adds_removes_and_excludes_experimental(self):
        self.add_skill('experimental', 'unfinished')
        self.assertEqual(self.sync().returncode, 0)
        for directory in self.destinations:
            self.assertEqual((directory / 'example').resolve(),
                             self.repo / 'skills/productivity/example')
            self.assertFalse((directory / 'unfinished').is_symlink())
            (directory / 'unrelated').symlink_to(self.base / 'external')
        repeat = self.sync()
        self.assertEqual(repeat.returncode, 0)
        self.assertEqual(repeat.stdout, '')
        shutil.rmtree(self.repo / 'skills/productivity/example')
        self.add_skill('productivity', 'new')
        self.assertEqual(self.sync().returncode, 0)
        for directory in self.destinations:
            self.assertFalse((directory / 'example').is_symlink())
            self.assertTrue((directory / 'new').is_symlink())
            self.assertTrue((directory / 'unrelated').is_symlink())

    def test_missing_source_preserves_links(self):
        self.assertEqual(self.sync().returncode, 0)
        (self.repo / 'skills').rename(self.repo / 'skills-unavailable')
        self.assertNotEqual(self.sync().returncode, 0)
        for directory in self.destinations:
            self.assertTrue((directory / 'example').is_symlink())

    def test_nested_skills_and_relocation(self):
        self.assertEqual(self.sync().returncode, 0)
        nested = self.repo / 'skills/engineering/delivery/deep group'
        nested.mkdir(parents=True)
        (self.repo / 'skills/productivity/example').rename(nested / 'example')
        self.add_skill('engineering/planning', 'plan')
        result = self.sync()
        self.assertEqual(result.returncode, 0, result.stderr)
        for directory in self.destinations:
            self.assertEqual((directory / 'example').resolve(), nested / 'example')
            self.assertEqual((directory / 'plan').resolve(),
                             self.repo / 'skills/engineering/planning/plan')
        repeat = self.sync()
        self.assertEqual(repeat.returncode, 0, repeat.stderr)
        self.assertEqual(repeat.stdout, '')

    def test_nested_duplicate_aborts_before_changing_links(self):
        self.assertEqual(self.sync().returncode, 0)
        self.add_skill('engineering/delivery', 'example')
        result = self.sync()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Duplicate skill name: example', result.stderr)
        self.assertEqual(result.stdout, '')
        for directory in self.destinations:
            self.assertEqual((directory / 'example').resolve(),
                             self.repo / 'skills/productivity/example')

    def test_recursive_discovery_skips_experimental_symlinks_and_skill_contents(self):
        self.add_skill('experimental/nested', 'unfinished')
        self.add_skill('productivity/example/assets', 'embedded')
        external = self.base / 'external'
        external.mkdir()
        (external / 'SKILL.md').write_text('test\n')
        (self.repo / 'skills/productivity/linked').symlink_to(external)
        (self.repo / 'skills/productivity/loop').symlink_to(self.repo / 'skills')
        result = self.sync()
        self.assertEqual(result.returncode, 0, result.stderr)
        for directory in self.destinations:
            self.assertEqual({path.name for path in directory.iterdir()}, {'example'})

    def test_existing_empty_source_removes_last_skill(self):
        self.assertEqual(self.sync().returncode, 0)
        shutil.rmtree(self.repo / 'skills/productivity')
        self.assertEqual(self.sync().returncode, 0)
        for directory in self.destinations:
            self.assertFalse((directory / 'example').is_symlink())

    def test_symlinked_destination_components_abort_before_any_writes(self):
        outside = self.base / 'outside'
        outside.mkdir()
        for relative in ('.agents', '.agents/skills', '.claude', '.claude/skills'):
            with self.subTest(destination=relative):
                link = self.repo / relative
                link.parent.mkdir(parents=True, exist_ok=True)
                link.symlink_to(outside, target_is_directory=True)
                result = self.sync()
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(list(outside.iterdir()), [])
                for directory in self.destinations:
                    self.assertFalse((directory / 'example').is_symlink())
                link.unlink()

    def test_conflict_in_second_destination_preserves_first(self):
        self.assertEqual(self.sync().returncode, 0)
        shutil.rmtree(self.repo / 'skills/productivity/example')
        self.add_skill('productivity', 'new')
        (self.destinations[1] / 'new').mkdir()
        self.assertNotEqual(self.sync().returncode, 0)
        for directory in self.destinations:
            self.assertTrue((directory / 'example').is_symlink())
        self.assertFalse((self.destinations[0] / 'new').is_symlink())


if __name__ == '__main__':
    unittest.main()
