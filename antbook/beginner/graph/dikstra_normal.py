INF = float('inf')

V, E = 0, 0
cost = []
d = []
# 最短が求まっているか否かがindex → Boolで格納される
used = []


def dikstra(s):
    d[s] = 0

    while True:
        # 次の最短経路を探す起点となる頂点を見つける
        v = -1
        for u in range(V):
            if not used[u] and (v == -1 or d[u] < d[v]):
                v = u

        if v == -1:
            break
        # 地点vからの最短距離は求めたことを保証する
        used[v] = True

        # 上記vから行ける最短経路uをそれぞれ格納する
        for u in range(V):
            # すでに別の起点vから最短経路が求まっている場合はそちら(d[u])を使用する
            # if d[u] > d[v]+cost[v→u]: d[u] = d[v]+cost[v→u]
            d[u] = min(d[u], d[v] + cost[v][u])


def resolve():
    global d, V, E, cost, used
    V, E = map(int, input().split(" "))
    cost = [[INF] * V for _ in range(V)]
    for _ in range(E):
        s, t, c = map(int, input().split(" "))
        # Start→Toまでの重さをそれぞれに格納
        cost[s][t] = c
        cost[t][s] = c

    d = [INF for _ in range(V)]
    used = [False] * V

    dikstra(0)
    print(d)


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
        input = """7 10
0 1 2
0 2 5
1 2 4
1 3 6
1 4 10
2 3 2
3 5 1
4 5 3
4 6 5
5 6 9"""
        output = """[0, 2, 5, 7, 11, 8, 16]"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 4
0 1 1
0 2 4
1 3 1
3 2 1"""
        output = """[0, 1, 3, 2]"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
