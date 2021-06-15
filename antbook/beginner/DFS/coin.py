# 500~1の硬貨をできるだけ少ない数使って支払う方法
def resolve():
    v = [1, 5, 10, 50, 100, 500]
    c = list(map(int, input().split(" ")))
    a = int(input())

    count = 0
    for i in reversed(range(0, 6)):
        t = min(a // v[i], c[i])
        a -= t * v[i]
        count += t
    print(count)


# if __name__ == "__main__":  # 提出時のみ復活させる
#     resolve()

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
        input = """3 2 1 3 0 2
620"""
        output = """6"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
