def resolve():
    n, A = map(int, input().split(" "))
    a = list(map(int, input().split(" ")))

    INF = 1000000
    dp = [[INF] * (A + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(A + 1):
            if j >= a[i]:
                dp[i + 1][j] = min(dp[i][j - a[i]] + 1, dp[i][j])
            else:
                dp[i + 1][j] = dp[i][j]
    if dp[n][A] == INF:
        print(-1)
    else:
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
        input = """2 6
7 5"""
        output = """-1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
