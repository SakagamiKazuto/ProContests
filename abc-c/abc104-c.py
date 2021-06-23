import re

D, G = 0, 0
P, C = [], []


def dfs(i, tc, t, to):
    # ベース・ケース
    if i < 0:
        return ""

    # 再帰ステップ
    point = 100 * (i + 1)
    for j in range(1, P[i] + 1):
        to += 1
        if j == P[i]:
            if (point * j + C[i]) + t >= G:
                tc.append(to)
                dfs(i - 1, tc, 0, 0)
            else:
                t += point * j + C[i]
                dfs(i - 1, tc, t, to)
                dfs(i - 1, tc, 0, 0)
        elif (point * j) + t >= G:
            tc.append(to)
            dfs(i - 1, tc, 0, 0)
    return tc


def resolve():
    global D, G, P, C
    D, G = map(int, input().split(" "))
    P, C = [], []
    for _ in range(D):
        p, c = map(int, input().split(" "))
        P.append(p)
        C.append(c)
    x = dfs(D - 1, [], 0, 0)
    print(min(x))


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

    def test_入力例_1(self):
        input = """2 700
3 500
5 800"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 2000
3 500
5 800"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2 400
3 500
5 800"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """5 25000
20 1000
40 1000
50 1000
30 1000
1 1000"""
        output = """66"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
