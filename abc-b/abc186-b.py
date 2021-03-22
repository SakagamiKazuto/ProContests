def resolve():
    h, w = map(int, input().split())
    a = []
    for _ in range(h):
        a.append(list(map(int, input().split())))

    min = minInArray(a, h, w)
    print(sumWith(a, min, h, w))


def minInArray(arr, h, w):
    min = 100
    for i in range(h):
        for j in range(w):
            if (arr[i][j] <= min):
                min = arr[i][j]
    return min


def sumWith(arr, min, h, w):
    count = 0
    for i in range(h):
        for j in range(w):
                count = count + arr[i][j] - min
    return count


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
        input = """2 3
2 2 3
3 2 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 3
99 99 99
99 0 99
99 99 99"""
        output = """792"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 2
4 4
4 4
4 4"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
