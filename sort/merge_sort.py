def resolve():
    arr = list(map(int, input().split()))
    ans = merge_sort(arr)
    for i, v in enumerate(ans):
        print(v, end=" ")

def merge_sort(arr):
    if len(arr) <= 1:
        return [arr[0]]

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left, right):
    merged = []
    l_i, r_i = 0, 0

    while l_i < len(left) and r_i < len(right):
        if left[l_i] <= right[r_i]:
            merged.append(left[l_i])
            l_i += 1
        else:
            merged.append(right[r_i])
            r_i += 1

    if l_i < len(left):
        merged.extend(left[l_i:])
    else:
        merged.extend(right[r_i:])
    return merged


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
