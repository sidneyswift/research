import importlib.util
import subprocess
import tempfile
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location('checker', Path(__file__).parents[1] / 'check-source-citations.py')
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class CitationContract(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.repo = self.root / 'repo'
        self.repo.mkdir()
        subprocess.run(['git', 'init', '-q', str(self.repo)], check=True)
        (self.repo / 'evidence.md').write_text('first\nsecond\n')
        checker.git(self.repo, 'add', '.')
        checker.git(self.repo, '-c', 'commit.gpgsign=false', '-c', 'core.hooksPath=/dev/null', '-c', 'user.name=Fixture', '-c', 'user.email=fixture@example.test', 'commit', '-qm', 'fixture')
        self.sha = checker.git(self.repo, 'rev-parse', 'HEAD').decode().strip()
        self.wiki = self.root / 'wiki'
        self.wiki.mkdir()
        subprocess.run(['git', 'init', '-q', str(self.wiki)], check=True)
        (self.wiki / 'sources').mkdir()
        self.source = self.wiki / 'sources/sample.md'
        self.write_source()
        (self.wiki / 'page.md').write_text('[[sources/sample#valid]]')
        checker.git(self.wiki, 'add', '.')

    def write_source(self, revision=None, path='evidence.md', bounds='L1-L2'):
        self.source.write_text(f'---\nurl: https://github.com/owner/repo\nupstream-commit: {self.sha}\n---\n'
                              f'## Anchor map\n### valid\n[x](https://github.com/owner/repo/blob/{revision or self.sha}/{path}#{bounds})\n')

    def errors(self):
        return checker.check(self.wiki, self.source, self.repo)[0]

    def test_valid_and_dirty_source_uses_pinned_blob(self):
        (self.repo / 'evidence.md').write_text('changed working tree\n')
        self.assertEqual([], self.errors())

    def test_missing_anchor(self):
        (self.wiki / 'page.md').write_text('[[sources/sample#typo]]')
        self.assertTrue(any('unregistered #typo' in e for e in self.errors()))

    def test_range_past_end(self):
        self.write_source(bounds='L1-L3')
        self.assertTrue(any('invalid lines' in e for e in self.errors()))

    def test_missing_blob(self):
        self.write_source(path='missing.md')
        self.assertTrue(any('missing or non-text' in e for e in self.errors()))

    def test_floating_revision(self):
        self.write_source(revision='main')
        self.assertTrue(any('unpinned' in e for e in self.errors()))

    def test_wrong_repository(self):
        self.source.write_text(self.source.read_text().replace('/owner/repo/blob/', '/other/repo/blob/'))
        self.assertTrue(any('unexpected repository' in e for e in self.errors()))

    def test_untracked_page_explicitly_included(self):
        page = self.wiki / 'new.md'
        page.write_text('[[sources/sample#unknown]]')
        self.assertEqual([], self.errors())
        errors, _ = checker.check(self.wiki, self.source, self.repo, [page])
        self.assertTrue(any('unregistered #unknown' in e for e in errors))


    def test_missing_explicit_page(self):
        errors, _ = checker.check(self.wiki, self.source, self.repo, [self.wiki / 'typo.md'])
        self.assertTrue(any('explicit page missing' in e for e in errors))

    def test_incidental_anchor_text_does_not_register(self):
        self.source.write_text(self.source.read_text() + 'Example mentions `#typo`.\n')
        (self.wiki / 'page.md').write_text('[[sources/sample#typo]]')
        self.assertTrue(any('unregistered #typo' in e for e in self.errors()))

    def test_fenced_heading_does_not_register(self):
        self.source.write_text(self.source.read_text() + '```md\n### typo\n```\n')
        (self.wiki / 'page.md').write_text('[[sources/sample#typo]]')
        self.assertTrue(any('unregistered #typo' in e for e in self.errors()))

    def test_heading_outside_map_does_not_register(self):
        self.source.write_text(self.source.read_text() + '## Other section\n### typo\n')
        (self.wiki / 'page.md').write_text('[[sources/sample#typo]]')
        self.assertTrue(any('unregistered #typo' in e for e in self.errors()))


if __name__ == '__main__':
    unittest.main()
