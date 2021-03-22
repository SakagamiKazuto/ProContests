def resolve():
    n = int(input())
    xy = []
    for _ in range(n):
        xy.append(list(map(int, input().split())))

    cnt = 0
    # for i in range(n):
        # for j in range(i):

    print(cnt)


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
        input = """3
0 0
1 2
2 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1
-691 273"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
-31 -35
8 -36
22 64
5 73
-14 8
18 -58
-41 -85
1 -88
-21 -85
-11 82"""
        output = """11"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
