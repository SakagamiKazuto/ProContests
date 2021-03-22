# zfill入れたら通ったナリ
def resolve():
    a, b, c = map(int, input().split())
    n = int(input())
    hm = []
    for i in range(n):
        hm.append(list(map(int, input().split())))
    hm = list(reversed(hm))
    for h, m in hm:
        if h == 8:
            if (m + b + c) < 60:
                print_ans(h, m, a)
                return
        else:
            print_ans(h, m, a)
            return


def print_ans(h, m, a):
    if m - a >= 0:
        print("0{0}:{1}".format(h, str(m - a).zfill(2)))
    else:
        print("0{0}:{1}".format(h - 1, str(60 + m - a).zfill(2)))


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
        input = """30 30 10
3
6 0
7 0
8 0"""
        output = """07:30"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 10 10
6
8 5
8 15
8 25
8 35
8 45
8 55"""
        output = """08:25"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 10 10
2
8 5
8 15"""
        output = """08:05"""
        self.assertIO(input, output)

    def test_境界値1(self):
        input = """30 30 30
2
6 0
8 59"""
        output = """05:30"""
        self.assertIO(input, output)

    def test_境界値2(self):
        input = """1 1 1
5
6 0
8 56
8 57
8 58
8 59"""
        output = """08:56"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
