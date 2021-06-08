# 2つ以上の隣接が存在する塊は全体でいくつか
import sys

sys.setrecursionlimit(2000)

def resolve():
    n = int(input())
    m = int(input())
    a = []
    for i in range(n):
        a.append(list(map(str, input().split())))

    def dfs(y, x):
        a[y][x] = "."

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx = x + dx
                ny = y + dy
                if (0 <= nx and nx < m and 0 <= ny and ny < n):
                    if (a[ny][nx] == 'W'):
                        dfs(nx, ny)
        return

    count = 0
    for y in range(n):
        for x in range(m):
            if a[y][x] == "W":
                dfs(y, x)
                count += 1
    print(count)


# a[i][j]いらんくね
# def dfs(a, w, i, j):
#     a[i][j] = "."
#
#     for k in range(i - 1, i + 2):
#         for l in range(j-1, j+2):
#             if a[i][j] == "W":
#                 dfs(a, a[k][l], i, j)
#     return


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
        input = """10
12
W . . . . . . . . W W . 
. W W W . . . . . W W W 
. . . . W W . . . W W . 
. . . . . . . . . W W . 
. . . . . . . . . W . . 
. . W . . . . . . W . . 
. W . W . . . . . W W . 
W . W . W . . . . . W . 
. W . W . . . . . . W . 
. . W . . . . . . . W ."""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
