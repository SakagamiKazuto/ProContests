def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    losses = 0
    for i in range(n):
        sumA = A[i] + A[i + 1]
        if B[i] >= sumA:
            losses += B[i] - sumA
            A[i+1] = 0
        else:
            if A[i] - B[i] < 0:
                A[i+1] -= B[i] - A[i]
        # 一応こうともかける(この例だと微妙かも)
        # losses += B[i] - sumA if B[i] >= sumA else 0
        # A[i + 1] = A[i + 1] - (B[i] - A[i]) if (A[i] - B[i] < 0) and B[i] < sumA else A[i + 1]

    print(sum(B) - losses)


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
        input = """2
3 5 2
4 5"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
5 6 3 8
5 100 8"""
        output = """22"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2
100 1 1
1 100"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
