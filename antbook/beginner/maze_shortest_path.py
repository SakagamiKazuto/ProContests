from collections import deque

INF = 1000000000

fields = """#S######.#
......#..#
.#.##.##.#
.#........
##.##.####
....#....#
.#######.#
....#.....
.####.###.
....#...G#""".split("\n")

n = 10  # N is Y
m = 10  # M is X

# start
sy = 0
sx = 1

# goal
gy = 9
gx = 8

# 4方向ベクトル ↑,→,↓,←
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

fs = []
for f in fields:
    fs.append(list(f))

# 各座標←→スタート間の最短距離
d = [[INF] * n for _ in range(m)]


def bfs():
    q = deque()

    q.append([sy, sx])
    d[sy][sx] = 0

    while len(q) != 0:
        p = q.popleft()
        # goal判断
        if p[0] == gy and p[1] == gx:
            break

        # 移動方向の判定と格納
        for i in range(4):
            by = dy[i] + p[0]
            bx = dx[i] + p[1]
            if (0 <= bx < m) and (0 <= by < n) and (fs[by][bx] != "#") and (d[by][bx] == INF):
                q.append([by, bx])
                d[by][bx] = d[p[0]][p[1]] + 1
    return d[gy][gx]


def resolve():
    print(bfs())


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
        input = """10 10
#S######.#
......#..#
.#.##.##.#
.#........
##.##.####
....#....#
.#######.#
....#.....
.####.###.
....#...G#"""
        output = """22"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
