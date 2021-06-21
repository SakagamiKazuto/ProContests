INF = float('inf')

V, E = 0, 0
cost = []
mincost = []
# 最短が求まっているか否かがindex → Boolで格納される
used = []


def prim(s):
    mincost[s] = 0
    res = 0

    while True:
        # 次の最短経路を探す起点となる頂点を見つける
        v = -1
        for u in range(V):
            if not used[u] and (v == -1 or mincost[u] < mincost[v]):
                v = u

        if v == -1:
            break
        # 地点vからの最短距離は求めたことを保証する
        used[v] = True
        res += mincost[v]

        # 上記vから行ける最短経路uをそれぞれ格納する
        for u in range(V):
            # すでに別の起点vから最短経路が求まっている場合はそちら(d[u])を使用する
            # if d[u] > d[v]+cost[v→u]: d[u] = d[v]+cost[v→u]
            mincost[u] = min(mincost[u], cost[v][u])
    return res


def resolve():
    global mincost, V, E, cost, used
    V, E = map(int, input().split(" "))
    cost = [[INF] * V for _ in range(V)]
    for _ in range(E):
        s, t, c = map(int, input().split(" "))
        # Start→Toまでの重さをそれぞれに格納
        cost[s][t] = c
        cost[t][s] = c

    mincost = [INF for _ in range(V)]
    used = [False] * V

    print(prim(0))


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
        input = """7 9
0 1 2
0 4 10
1 2 1
1 3 3
1 5 7
3 5 1
3 6 5
4 5 5
5 6 8"""
        output = """17"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
