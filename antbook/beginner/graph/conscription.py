from common.union_find import UnionFind

N, M, R = 0, 0, 0
V = 0
es = []

def kruskal():
    es.sort()
    uf = UnionFind(V)
    res = 0
    for e in es:
        if not uf.same(e[1], e[2]):
            uf.union(e[1], e[2])
            res += e[0]
    return res

def resolve():
    global N, M, R, V
    N, M, R = map(int, input().split(" "))
    V = N + M
    for _ in range(R):
        x, y, d = map(int, input().split())
        # -d →高いdほど低くする, N+x →有向森化のためN+yでもよい
        es.append([-d, N + x, y])
    max_cost = 10000 * V
    print(max_cost + kruskal())


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
        input = """5 5 8
4 3 6831
1 3 4583
0 0 6592
0 1 3063
3 3 4975
1 3 2049
4 2 2104
2 2 781"""
        output = """71071"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
