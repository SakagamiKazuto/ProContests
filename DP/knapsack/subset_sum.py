def resolve():
    n, A = map(int, input().split(" "))
    a = list(map(int, input().split(" ")))

    dp = [[False] * (A + 1) for _ in range(n + 1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(A + 1):
            if j >= a[i]:
                dp[i + 1][j] = dp[i][j - a[i]] or dp[i][j]
            else:
                dp[i+1][j] = dp[i][j]
    if dp[n][A]:
        print("Yes")
    else:
        print("No")


# if __name__ == "__main__":
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
        input = """3 10
7 5 3"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 6
9 7"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
