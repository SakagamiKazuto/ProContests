import sys

sys.setrecursionlimit(1000000)

H, W = 0, 0
C = []
used = []


def in_area(dh, dw):
    return (0 <= dh < H) and (0 <= dw < W)


def dfs(h, w):
    # if C[h][w] == "g":
    #     return True

    used[h][w] = True
    # 4方向ベクトル ↑,→,↓,←
    dhw = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    # 再帰ステップ
    for hw in dhw:
        i = h + hw[0]
        j = w + hw[1]
        if in_area(i, j) and not used[i][j] and C[i][j] != "#":
            dfs(i, j)

    # # ベース・ケース
    # return False


def resolve():
    global H, W, C, used
    C, used = [], []
    H, W = map(int, input().split(" "))
    for _ in range(H):
        C.append(list(input()))
    used = [[False] * W for _ in range(H)]

    for h in range(H):
        for w in range(W):
            if C[h][w] == "s":
                dfs(h, w)

    for h in range(H):
        for w in range(W):
            if C[h][w] == "g":
                if used[h][w]:
                    print("Yes")
                else:
                    print("No")


if __name__ == "__main__":  # 提出時のみ復活させる
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

    #     def test_入力例1(self):
    #         input = """4 5
    # s####
    # ....#
    # #####
    # #...g"""
    #         output = """No"""
    #         self.assertIO(input, output)

    def test_入力例2(self):
        input = """4 4
...s
....
....
.g.."""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """10 10
s.........
#########.
#.......#.
#..####.#.
##....#.#.
#####.#.#.
g.#.#.#.#.
#.#.#.#.#.
###.#.#.#.
#.....#..."""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """10 10
s.........
#########.
#.......#.
#..####.#.
##....#.#.
#####.#.#.
g.#.#.#.#.
#.#.#.#.#.
#.#.#.#.#.
#.....#..."""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例5(self):
        input = """1 10
s..####..g"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
