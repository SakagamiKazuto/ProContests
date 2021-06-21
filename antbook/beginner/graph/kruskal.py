from common.union_find import UnionFind

V, E = 0, 0
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
    global V, E
    V, E = map(int, input().split(" "))
    for _ in range(E):
        s, t, c = map(int, input().split())
        es.append([c, s, t])
    print(kruskal())


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
