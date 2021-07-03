def resolve():
    N, W = map(int, input().split(" "))
    w = list(map(int, input().split(" ")))
    v = list(map(int, input().split(" ")))
    dp = [[0] * (W + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(W + 1):
            if j >= w[i]:
                dp[i + 1][j] = max(dp[i][j - w[i]] + v[i], dp[i][j])
            else:
                dp[i + 1][j] = dp[i][j]
    print(dp[N][W])


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
        input = """4 5
2 1 3 2
3 2 4 2"""
        output = """7"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
