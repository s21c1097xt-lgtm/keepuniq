import subprocess
import sys
import unittest
from pathlib import Path

COMMAND = Path(__file__).resolve().parents[1] / "keepuniq"


class TestKeepuniq(unittest.TestCase):

    def run_command(self, input_text):
        return subprocess.run(
            [sys.executable, str(COMMAND)],
            input=input_text,
            text=True,
            capture_output=True,
            check=True,
        )

    def test_remove_duplicates(self):
        result = self.run_command("apple\nbanana\napple\n")
        self.assertEqual(result.stdout, "apple\nbanana\n")

    def test_preserve_order(self):
        result = self.run_command("orange\napple\nbanana\napple\n")
        self.assertEqual(result.stdout, "orange\napple\nbanana\n")

    def test_empty_input(self):
        result = self.run_command("")
        self.assertEqual(result.stdout, "")

    def test_single_line(self):
        result = self.run_command("apple\n")
        self.assertEqual(result.stdout, "apple\n")

    def test_blank_lines(self):
        result = self.run_command("apple\n\napple\n")
        self.assertEqual(result.stdout, "apple\n\n")


if __name__ == "__main__":
    unittest.main()
