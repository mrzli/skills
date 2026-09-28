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

    def sync(self):
        return subprocess.run(
            ['bash', str(self.repo / 'scripts/sync-skills.sh')],
            cwd=self.base, capture_output=True, text=True,
        )

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
