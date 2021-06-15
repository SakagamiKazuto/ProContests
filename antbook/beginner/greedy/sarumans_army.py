def resolve():
    n = int(input())
    R = int(input())
    X = list(map(int, input().split(" ")))

    ans = 0
    i = 0
    while i < n:
        s = X[i]
        while i < n and X[i] <= s + R:
            i += 1
        p = X[i-1]
        while i < n and X[i] <= p + R:
            i += 1
        ans += 1
    print(ans)


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
        input = """6
10
1 7 15 20 30 50"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
