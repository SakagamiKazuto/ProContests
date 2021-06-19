MAX_V = 1000

V, E = 0, 0
# 1層目がStart, 2層目がToで頂点間の結びつきを表現する
G = [[] for _ in range(MAX_V)]
color = [0] * MAX_V


def dfs(v, c):
    color[v] = c

    for i in range(len(G[v])):
        if color[G[v][i]] == c:
            return False
        if color[G[v][i]] == 0 and not dfs(G[v][i], -c):
            return False
    return True


def resolve():
    global V, E, G, color
    # テスト・ケース間で共通変数参照してるため一度変数を初期化する
    G = [[] for _ in range(MAX_V)]
    color = [0] * MAX_V

    V = int(input())
    E = int(input())
    for i in range(E):
        s, t = map(int, input().split(" "))
        G[s].append(t)
        G[t].append(s)

    for i in range(V):
        if color[i] == 0:
            if not dfs(i, 1):
                print("No")
                return
    print("Yes")


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
        input = """3
3
0 1
0 2
1 2"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
4
0 1
0 3
1 2
2 3"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
