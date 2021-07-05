def resolve():
    n, K = map(int, input().split(" "))
    a = list(map(int, input().split(" ")))
    m = list(map(int, input().split(" ")))

    dp = [-1 for _ in range(K + 1)]
    dp[0] = 0
    for i in range(n):
        for j in range(K + 1):
            if dp[j] >= 0:
                dp[j] = m[i]
            elif j < a[i] or dp[j - a[i]] <= 0:
                dp[j] -= 1
            else:
                dp[j] = dp[j - a[i]] - 1
    if dp[K] >= 0:
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
        input = """3 17
3 5 8
3 2 2"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
