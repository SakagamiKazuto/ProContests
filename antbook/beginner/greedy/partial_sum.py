# 整数aが与えられる。その中からいくつか選んで,その和をちょうどkに出来るか判定
def resolve():
    n = int(input())
    a = list(map(int, input().split()))
    k = int(input())
    if partial_sum(n, a, k, 0, 0):
        print("Yes")
    else:
        print("No")


def partial_sum(n, a, k, i, sum):
    if i == n:
        return sum == k

    # a[i]を足すパターン
    if partial_sum(n, a, k, i + 1, sum + a[i]):
        return True

    # a[i]を足さないパターン
    if partial_sum(n, a, k, i + 1, sum):
        return True

    return False


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
        input = """4
1 2 4 7
13"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
1 2 4 7
15"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
