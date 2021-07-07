def resolve():
    n = int(input())
    p = list(map(int, input().split(" ")))
    w = sum(p)
    dp = [[False] * (w + 1) for _ in range(n + 1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(w + 1):
            if j - p[i] < 0:
                dp[i + 1][j] = dp[i][j]
            else:
                dp[i + 1][j] = dp[i][j - p[i]] or dp[i][j]
    ans = 0
    for j in range(w + 1):
        if dp[n][j]:
            ans += 1
    print(ans)

if __name__ == "__main__":
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

    def test_Sample_Input_1(self):
        input = """3
2 3 5"""
        output = """7"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10
1 1 1 1 1 1 1 1 1 1"""
        output = """11"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
