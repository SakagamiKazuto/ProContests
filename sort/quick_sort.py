def resolve():
    arr = list(map(int, input().split()))
    ans = quick_sort(arr)
    for i, v in enumerate(ans):
        print(v, end=" ")

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    ref = arr[0]
    ref_count = 0
    left, right = [], []

    for v in arr:
        if v < ref:
            left.append(v)
        elif v > ref:
            right.append(v)
        else:
            ref_count += 1

    left = quick_sort(left)
    right = quick_sort(right)
    return left + [ref] * ref_count + right

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
        input = """3 5 2 6 4 8 1 9 5"""
        output = """1 2 3 4 5 5 6 8 9"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 5 2 6 4 8 1 9"""
        output = """1 2 3 4 5 6 8 9"""
        self.assertIO(input, output)

    # def test_入力例_3(self):
    #     input = """12 15"""
    #     output = """No"""
    #     self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
