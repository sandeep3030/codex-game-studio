
"""Basic tests for the Codex Game Studio validator."""

from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = ROOT / "scripts" / "validate-studio.py"


class StudioValidationTests(unittest.TestCase):

    def test_validator_exists(self):
        self.assertTrue(VALIDATOR.is_file())

    def test_required_directories_exist(self):
        directories = [
            ".agents/skills",
            ".codex/agents",
            "engines/godot",
            "design/templates",
            "studio",
            "scripts",
            "tests/studio-tests",
            "examples",
        ]

        for directory in directories:
            with self.subTest(directory=directory):
                self.assertTrue((ROOT / directory).is_dir())

    def test_repository_validation(self):
        result = subprocess.run(
            [sys.executable, str(VALIDATOR)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(
            result.returncode,
            0,
            msg=result.stdout + result.stderr,
        )
        self.assertIn("VALIDATION PASSED", result.stdout)


if __name__ == "__main__":
    unittest.main()
