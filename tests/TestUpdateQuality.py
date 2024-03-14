import subprocess
import unittest


class TestUpdateQuality(unittest.TestCase):
    def test_golden_master(self):
        actual = subprocess.run("python3 ../texttest_fixture.py 30",
                                shell=True,
                                capture_output=True,
                                text=True)
        assert read_file("../reference-30-days.txt") == actual.stdout


def read_file(path):
    with open(path) as f:
        return f.read()


if __name__ == '__main__':
    unittest.main()
