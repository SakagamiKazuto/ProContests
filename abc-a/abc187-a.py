# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def resolve():
    # 入力:A B
    # 受け取った文字列を文字列として扱う
    # それぞれの配列の中身を足す
    # 比較して答え
    a, b = map(list, input().split())
    x = list(map(int, a))
    y = list(map(int, b))

    if (sum(x) >= sum(y)):
        print(str(sum(x)))
    else:
        print(str(sum(y)))


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
        input = """123 234"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """593 953"""
        output = """17"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100 999"""
        output = """27"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
