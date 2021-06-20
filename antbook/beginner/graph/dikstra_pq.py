import heapq

INF = float('inf')

V, E = 0, 0
G = []
d = []


def dikstra(s):
    d[s] = 0
    pq = []
    heapq.heappush(pq, (0, s))

    while len(pq) > 0:
        p = heapq.heappop(pq)
        v = p[1]
        # ??
        if d[v] < p[0]:
            continue

        for i in range(len(G[v])):
            # 変更したデータ構造では[[t c], [t c]...]のように隣接・重さが格納されている
            edge = G[v][i]
            to, cost = edge[0], edge[1]
            # 答え出力用のd[]以外に,pqにも最小値情報を入れておくことで冒頭のp=heapq.heappop()で取出し高速化実現
            if d[to] > d[v] + cost:
                d[to] = d[v] + cost
                heapq.heappush(pq, (d[to], to))

def resolve():
    global d, V, E, G
    V, E = map(int, input().split(" "))
    G = [[] for _ in range(V)]
    for _ in range(E):
        s, t, c = map(int, input().split(" "))
        # Start→Toまでの重さをそれぞれに格納
        G[s].append([t, c])
        G[t].append([s, c])

    d = [INF for _ in range(V)]

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
