def resolve():
    n, A = map(int, input().split(" "))
    a = list(map(int, input().split(" ")))

    dp = [[0] * (A + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(A + 1):
            if j >= a[i]:
                dp[i + 1][j] = dp[i][j - a[i]] + dp[i][j]
            else:
                dp[i+1][j] = dp[i][j]
    print(dp[n][A])


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
        input = """5 12
7 5 3 1 8"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 5
4 1 1 1"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
