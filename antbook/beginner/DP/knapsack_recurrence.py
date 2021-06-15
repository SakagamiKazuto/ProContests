def resolve():
    MAX_N = 100
    MAX_W = 10000
    dp = [[0] * (MAX_W + 1) for _ in range(MAX_N + 1)]  # メモ化テーブル
    n = int(input())
    w = int(input())
    wv = []
    for i in range(n):
        wv.append(list(map(int, input().split(" "))))

    # 末端からループを回す
    for node in range(n - 1, -1, -1):
        # 表の列のすべての要素において"ベストな付加価値の値"を探す
        for w_rest in range(w + 1):
            if w_rest < wv[node][0]:
                dp[node][w_rest] = dp[node + 1][w_rest]
            else:
                # 足す・足さないで付加価値が大きくなるほうをnodeのベストな値として登録する
                dp[node][w_rest] = max(dp[node + 1][w_rest], dp[node + 1][w_rest - wv[node][0]] + wv[node][1])

    print(dp[0][w])


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
