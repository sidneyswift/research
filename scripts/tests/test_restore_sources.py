"""Exercise reconstruction and preservation using local Git fixtures only."""
import contextlib
import importlib.util
import io
from pathlib import Path
import subprocess
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "restore-sources.py"
spec = importlib.util.spec_from_file_location("restore_sources", SCRIPT)
restore_sources = importlib.util.module_from_spec(spec)
spec.loader.exec_module(restore_sources)


class RestoreTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.origin = self.root / "origin"
        self.sources = self.root / "sources"
        self.sources.mkdir()
        self.git("init", "--quiet", self.origin)
        self.git("config", "user.name", "Fixture", cwd=self.origin)
        self.git("config", "user.email", "fixture@example.invalid", cwd=self.origin)
        (self.origin / "evidence.txt").write_text("original\n")
        self.git("add", ".", cwd=self.origin)
        self.git("commit", "--quiet", "-m", "fixture", cwd=self.origin)
        self.pin = self.git("rev-parse", "HEAD", cwd=self.origin)
        self.row = {"slug": "fixture--source", "url": self.origin.as_uri(), "commit": self.pin}

    def git(self, *args, cwd=None):
        return subprocess.check_output(["git", *map(str, args)], cwd=cwd, text=True, stderr=subprocess.PIPE).strip()

    def restore(self, **kwargs):
        with contextlib.redirect_stdout(io.StringIO()):
            restore_sources.restore(self.row, self.sources, **kwargs)

    def test_clone_exact_pin_and_repeat(self):
        self.restore()
        dest = self.sources / self.row["slug"]
        self.assertEqual(self.git("rev-parse", "HEAD", cwd=dest), self.pin)
        self.assertEqual((dest / "evidence.txt").read_text(), "original\n")
        self.restore()
        self.restore(check=True)

    def test_preserves_dirty_checkout(self):
        self.restore()
        dest = self.sources / self.row["slug"]
        (dest / "evidence.txt").write_text("local work\n")
        (dest / "untracked.txt").write_text("also keep\n")
        self.restore(pull=True)
        self.assertEqual((dest / "evidence.txt").read_text(), "local work\n")
        self.assertEqual((dest / "untracked.txt").read_text(), "also keep\n")

    def test_mismatched_head_fails_without_checkout(self):
        self.restore()
        dest = self.sources / self.row["slug"]
        self.row["commit"] = "0" * 40
        with self.assertRaisesRegex(ValueError, "differs from pin"):
            self.restore()
        self.assertEqual(self.git("rev-parse", "HEAD", cwd=dest), self.pin)

    def test_check_missing_does_not_create(self):
        with self.assertRaisesRegex(ValueError, "missing"):
            self.restore(check=True)
        self.assertEqual(list(self.sources.iterdir()), [])

    def test_plain_directory_is_preserved(self):
        dest = self.sources / self.row["slug"]
        dest.mkdir()
        (dest / "keep").write_text("unique")
        with self.assertRaisesRegex(ValueError, "not an independent Git checkout"):
            self.restore()
        self.assertEqual((dest / "keep").read_text(), "unique")

    def test_failed_fetch_cleans_partial_clone(self):
        self.row["commit"] = "0" * 40
        with self.assertRaises(subprocess.CalledProcessError):
            self.restore()
        self.assertEqual(list(self.sources.iterdir()), [])

    def test_manifest_validation(self):
        manifest = self.root / "manifest.tsv"
        header = "slug\turl\tcommit\n"
        line = f"fixture--source\t{self.origin.as_uri()}\t{self.pin}\n"
        manifest.write_text(header + line)
        self.assertEqual(restore_sources.load_manifest(manifest), [self.row])
        for body in [line + line, line.replace("fixture--source", "../escape"), line.replace(self.pin, self.pin[:7])]:
            manifest.write_text(header + body)
            with self.assertRaises(ValueError):
                restore_sources.load_manifest(manifest)

    def test_subset_and_unknown_source(self):
        manifest = self.root / "manifest.tsv"
        manifest.write_text("slug\turl\tcommit\n" + f"fixture--source\t{self.origin.as_uri()}\t{self.pin}\n" + f"missing--source\tfile:///does-not-exist\t{self.pin}\n")
        command = ["python3", str(SCRIPT), "--manifest", str(manifest), "--sources-dir", str(self.sources), "--only"]
        good = subprocess.run(command + ["fixture--source"], capture_output=True, text=True)
        self.assertEqual(good.returncode, 0, good.stdout + good.stderr)
        self.assertFalse((self.sources / "missing--source").exists())
        bad = subprocess.run(command + ["unknown"], capture_output=True, text=True)
        self.assertNotEqual(bad.returncode, 0)

    def test_preserves_additional_historical_evidence(self):
        historical = self.pin
        (self.origin / "evidence.txt").write_text("new revision\n")
        self.git("add", ".", cwd=self.origin)
        self.git("commit", "--quiet", "-m", "new fixture", cwd=self.origin)
        self.row["commit"] = self.git("rev-parse", "HEAD", cwd=self.origin)
        self.row["evidence_commits"] = historical
        self.restore()
        dest = self.sources / self.row["slug"]
        self.assertEqual(self.git("show", historical + ":evidence.txt", cwd=dest), "original")
        self.assertEqual(self.git("rev-parse", "HEAD", cwd=dest), self.row["commit"])
        self.restore(check=True)


if __name__ == "__main__":
    unittest.main()
