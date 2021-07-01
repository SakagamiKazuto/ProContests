import sys
sys.setrecursionlimit(10**6)

graph = []
color = []


def dfs(index, c):
    color[index] = c
    for g in graph[index]:
        if color[g[0]] == 0:
            if g[1] % 2 != 0:
                dfs(g[0], -1 * c)
            else:
                dfs(g[0], c)


def resolve():
    global graph, color
    n = int(input())
    graph = [[] for _ in range(n)]
    color = [0 for _ in range(n)]
    for i in range(1, n):
        u, v, w = map(int, input().split(" "))
        graph[u - 1].append([v - 1, w])
        graph[v - 1].append([u - 1, w])
    dfs(0, -1)
    c_rep = [0 if c == -1 else c for c in color]
    print(*c_rep, sep="\n")


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

    #     def test_入力例_1(self):
    #         input = """3
    # 1 2 2
    # 2 3 1"""
    #         output = """0
    # 0
    # 1"""
    #         self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
1 2 2
1 3 1
"""
        output = """0
0
1"""
        self.assertIO(input, output)


#     def test_入力例_2(self):
#         input = """5
# 2 5 2
# 2 3 10
# 1 3 8
# 3 4 2"""
#         output = """1
# 0
# 1
# 0
# 1"""
#         self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
