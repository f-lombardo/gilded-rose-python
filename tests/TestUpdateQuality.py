import subprocess
import unittest
from io import StringIO

from texttest_fixture import run_program


class TestUpdateQuality(unittest.TestCase):
    def test_golden_master_from_outside(self):
        actual = subprocess.run("python3 ../texttest_fixture.py 30",
                                shell=True,
                                capture_output=True,
                                text=True)
        assert read_file("../reference-30-days.txt") == actual.stdout

    def test_golden_master_from_inside(self):
        stdout = StringIO()
        run_program(stdout, ["ignored_program_name", 30])
        assert read_file("../reference-30-days.txt") == stdout.getvalue()


def read_file(path):
    with open(path) as f:
        return f.read()


if __name__ == '__main__':
    unittest.main()
