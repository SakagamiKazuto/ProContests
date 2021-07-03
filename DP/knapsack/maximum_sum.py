# 最大和問題

def resolve():
    l = list(map(int, input().split(" ")))
    n = len(l)
    dp = [-10000 for _ in range(100)]
    dp[0] = 0
    for i in range(n):
        # もし足さなかったとき VS もし足したとき
        dp[i + 1] = max(dp[i], dp[i] + l[i])
    print(dp[n])


# 再帰
# n = 0
# l = []
#
# dp = []
# def dfs(i, total):
#     # ベースケース
#     if i == n:
#         return total
#
#     # 再帰ステップ
#     return max(dfs(i + 1, total + l[i]), dfs(i + 1, total))
#
#
# def resolve():
#     global n, l
#     l = list(map(int, input().split(" ")))
#     n = len(l)
#     print(dfs(0, 0))


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
        input = """3 -7 5"""
        output = """8"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
