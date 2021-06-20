import heapq

INF = float('inf')

N, R = 0, 0
G = []
d = []
d2 = []


def dikstra(s):
    d[s] = 0
    pq = []
    heapq.heappush(pq, (0, s))

    while len(pq) > 0:
        p = heapq.heappop(pq)
        v = p[1]
        # ??
        if d2[v] < p[0]:
            continue

        for i in range(len(G[v])):
            # 変更したデータ構造では[[t c], [t c]...]のように隣接・重さが格納されている
            edge = G[v][i]
            to, cost = edge[0], edge[1]
            dist = d[v] + cost
            # 答え出力用のd[]以外に,pqにも最小値情報を入れておくことで冒頭のp=heapq.heappop()で取出し高速化実現
            if d[to] > dist:
                d[to], dist = dist, d[to]
                heapq.heappush(pq, (d[to], to))
            if d2[to] > dist > d[to]:
                d2[to] = dist
                heapq.heappush(pq, (d2[to], to))


def resolve():
    global d, d2, N, R, G
    N, R = map(int, input().split(" "))
    G = [[] for _ in range(N)]
    for _ in range(R):
        s, t, c = map(int, input().split(" "))
        s -= 1
        t -= 1
        # Start→Toまでの重さをそれぞれに格納
        G[s].append([t, c])
        G[t].append([s, c])

    d = [INF for _ in range(N)]
    d2 = [INF for _ in range(N)]

    dikstra(0)
    print(d2[N - 1])


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
        input = """4 4
1 2 100
2 3 250
2 4 200
3 4 100"""
        output = """450"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
