from collections import deque

INF = 100000000

H, W = 0, 0
Fields = []
d = []


def is_goal(p, g):
    return p[0] == g[0] and p[1] == g[1]


def in_area(dh, dw):
    return (0 <= dh < H) and (0 <= dw < W)


def bfs(s, g):
    q = deque()
    # ↑, →, ↓, ←
    vector = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    q.append(s)
    d[s[0]][s[1]] = 0

    while len(q) != 0:
        p = q.popleft()
        py = p[0]
        px = p[1]

        if is_goal(p, g):
            break

        for v in vector:
            y = py + v[0]
            x = px + v[1]
            if in_area(y, x) and Fields[y][x] != "#" and d[y][x] == INF:
                d[y][x] = d[py][px] + 1
                q.append([y, x])
    return d[g[0]][g[1]]


def resolve():
    global H, W, Fields, d
    H, W = map(int, input().split(" "))
    sy, sx = map(int, input().split(" "))
    s = [sy - 1, sx - 1]
    gy, gx = map(int, input().split(" "))
    g = [gy - 1, gx - 1]
    Fields = []
    for _ in range(H):
        Fields.append(list(input()))
    d = [[INF] * W for _ in range(H)]
    print(bfs(s, g))


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

    def test_入力例1(self):
        input = """7 8
2 2
4 5
########
#S.....#
#.######
#..#G..#
#..##..#
##.....#
########"""
        output = """11"""
        self.assertIO(input, output)


    def test_入力例2(self):
        input = """5 8
2 2
2 4
########
#.#....#
#.###..#
#......#
########"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """50 50
2 2
49 49
##################################################
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
##################################################"""
        output = """94"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
