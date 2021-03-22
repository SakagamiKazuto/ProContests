import math


def resolve():
    n = int(input())
    al = list((map(int, input().split(" "))))
    sum = 0
    for i in range(1, n):
        subA = al[i - 1] - al[i]
        if subA > 0:
            al[i] += subA
            sum += subA
    print(sum)


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
        input = """5
2 1 5 4 3"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
3 3 3 3 3"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
