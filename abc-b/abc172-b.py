import math


def resolve():
    s = str(input())
    t = str(input())
    c = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            c += 1
    print(c)


if __name__ == "__main__":
    resolve()

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
        input = """cupofcoffee
cupofhottea"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """abcde
bcdea"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """apple
apple"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
