from common.union_find import UnionFind

n = 0
c_f_t = []


def kruskal():
    c_f_t.sort()
    uf = UnionFind(n)
    res = 0
    for e in c_f_t:
        if not uf.same(e[1], e[2]):
            uf.union(e[1], e[2])
            res += e[0]
    return res


def resolve():
    global c_f_t, n
    c_f_t = []

    n = int(input())
    id_xy = []
    for i in range(n):
        x, y = map(int, input().split(" "))
        id_xy.append([i, x, y])

    for i in range(n):
        for j in range(i, n):
            cost = min(abs(id_xy[i][1] - id_xy[j][1]), abs(id_xy[i][2] - id_xy[j][2]))
            c_f_t.append([cost, id_xy[i][0], id_xy[j][0]])
    print(kruskal())


if __name__ == "__main__":
    resolve()

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
        input = """3
1 5
3 9
7 8"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6
8 3
4 9
12 19
18 1
13 5
7 6"""
        output = """8"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
