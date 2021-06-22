s = []


def dfs(i, c):
    if i == len(s) - 1:
        return sum(list(map(int, c.split("+"))))
    return dfs(i + 1, c + s[i + 1]) + dfs(i + 1, c + "+" + s[i + 1])


def resolve():
    global s
    s = input()
    print(dfs(0, s[0]))


if __name__ == "__main__":  # 提出時のみ復活させる
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
        input = """125"""
        output = """176"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """9999999999"""
        output = """12656242944"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
