T = []
N = 0


def dfs(i, sum1, sum2):
    # ベースケース
    if i == N:
        return max(sum1, sum2)

    # 再帰ステップ
    return min(dfs(i + 1, sum1 + T[i], sum2), dfs(i + 1, sum1, sum2 + T[i]))


def resolve():
    global T, N
    N = int(input())
    T = []
    for _ in range(N):
        T.append(int(input()))
    print(dfs(0, 0, 0))


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

    def test_入力例1(self):
        input = """4
4
6
7
10"""
        output = """14"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """3
1
2
4"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """1
29"""
        output = """29"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
