import sys

sys.setrecursionlimit(1000000)

H, W = 10, 10
A = []
used = []


# "1つだけ埋めるとしたら"の仮定すっ飛ばしてたのがすべての間違いだった...
def in_area(dh, dw):
    return (0 <= dh < H) and (0 <= dw < W)


def dfs(h, w, is_normal, filled):
    used[h][w] = True
    # 4方向ベクトル ↑,→,↓,←
    dhw = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    # 再帰ステップ
    # if not filled:
    for hw in dhw:
        i = h + hw[0]
        j = w + hw[1]
        if is_normal:
            if in_area(i, j) and not used[i][j] and A[i][j] == "o":
                dfs(i, j, True, filled)
            if in_area(i, j) and not used[i][j] and A[i][j] == "x":
                dfs(i, j, False, filled)
        else:
            if in_area(i, j) and not used[i][j] and A[i][j] == "o":
                A[h][w] = "o"
                dfs(i, j, True, True)


def resolve():
    global H, W, A, used
    A, used = [], []
    for _ in range(H):
        A.append(list(input()))
    used = [[False] * W for _ in range(H)]

    count = 0
    for h in range(H):
        for w in range(W):
            if not used[h][w] and A[h][w] == "o":
                dfs(h, w, True, False)
                count += 1

    if count == 1:
        print("YES")
    else:
        print("NO")



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
        input = """xxxxxxxxxx
xoooooooxx
xxoooooxxx
xxxoooxxxx
xxxxoxxxxx
xxxxxxxxxx
xxxxoxxxxx
xxxoooxxxx
xxoooooxxx
xxxxxxxxxx"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """xxxxxxxxxx
xoooooooxx
xxoooooxxx
xxxoooxxxx
xxxxxxxxxx
xxxxxxxxxx
xxxxxxxxxx
xxxoooxxxx
xxoooooxxx
xxxxxxxxxx"""
        output = """NO"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """xxxxoxxxxx
xxxxoxxxxx
xxxxoxxxxx
xxxxoxxxxx
ooooxooooo
xxxxoxxxxx
xxxxoxxxxx
xxxxoxxxxx
xxxxoxxxxx
xxxxoxxxxx"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """xxxxxxxxxx
oooooooooo
xxxxxxxxxx
oooooooooo
xxxxxxxxxx
oooooooooo
xxxxxxxxxx
oooooooooo
xxxxxxxxxx
oooooooooo"""
        output = """NO"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
