def resolve():
    n = int(input())
    a = list(map(int, input().split(" ")))
    dp = [0 for _ in range(n + 1)]
    for i in range(n):
        dp[i] = 1
        for j in range(i):
            if a[j] < a[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(max(dp))


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
        input = """5
4 2 3 1 5"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
