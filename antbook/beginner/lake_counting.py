# 2つ以上の隣接が存在する塊は全体でいくつか
field_x_length = 10
field_y_length = 12

fields = """W . . . . . . . . W W .
. W W W . . . . . W W W
. . . . W W . . . W W .
. . . . . . . . . W W .
. . . . . . . . . W . .
. . W . . . . . . W . .
. W . W . . . . . W W .
W . W . W . . . . . W .
. W . W . . . . . . W .
. . W . . . . . . . W .""".split("\n")
fs = []
for f in fields:
    fs.append(list(f.split(" ")))


def dfs(x, y):
    fs[x][y] = '.'
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            nx = x + dx
            ny = y + dy
            if (0 <= nx and nx < field_x_length and 0 <= ny and ny < field_y_length and fs[nx][ny] == 'W'):
                dfs(nx, ny)

def resolve():
    lake_count = 0
    for i in range(0, field_x_length):
        for j in range(0, field_y_length):
            if (fs[i][j] == 'W'):
                dfs(i, j)
                lake_count += 1
    print(lake_count)

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
