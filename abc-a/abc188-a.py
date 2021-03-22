# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def resolve():
    x, y = map(int, input().split())
    if (abs(x - y) < 3):
        print("Yes")
    else:
        print("No")


import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """3 5"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """16 2"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """12 15"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
