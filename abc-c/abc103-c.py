import re

s = ""


def dfs(i, c):
    # もしlistの中を+-で切った合計が7なら配列をreturn
    if i == 3:
        if eval(c) == 7:
            return c
        else:
            return ""

    om = dfs(i + 1, c + "-" + s[i + 1])
    if om != "":
        return om

    op = dfs(i + 1, c + "+" + s[i + 1])
    if op != "":
        return op
    return ""


def resolve():
    global s
    s = input()
    print(dfs(0, s[0]) + "=7")


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
        input = """1222"""
        output = """1+2+2+2=7"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """0290"""
        output = """0-2+9+0=7"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3242"""
        output = """3-2+4+2=7"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
