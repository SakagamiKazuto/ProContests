MAX_N = 100
MAX_W = 10000
dp = [[-1] * (MAX_W + 1) for _ in range(MAX_N + 1)]  # メモ化テーブル


def knapsack(node, w_rest, n, w, wv):
    if dp[node][w_rest] >= 0:
        return dp[node][w_rest]

    if node == n:
        res = 0
    elif w_rest < wv[node][0]:
        res = knapsack(node + 1, w_rest, n, w, wv)
    # 基本的にはここが呼ばれる
    else:
        # 足さない・足すパターン両方再帰的に呼び出す
        res = max(knapsack(node + 1, w_rest, n, w, wv),
                  knapsack(node + 1, w_rest - wv[node][0], n, w, wv) + wv[node][1])
    dp[node][w_rest] = res
    return res


def resolve():
    n = int(input())
    w = int(input())
    wv = []
    for i in range(n):
        wv.append(list(map(int, input().split(" "))))
    print(knapsack(0, w, n, w, wv))


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
        input = """4
5
2 3
1 2
3 4
2 2"""
        output = """7"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
