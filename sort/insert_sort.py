def resolve():
    arr = list(map(int, input().split()))
    ans = insert_sort(arr)
    for i, v in enumerate(ans):
        print(v, end=" ")


def insert_sort(arr):
    # for i in range(1, len(arr)):
    for i in range(1, len(arr)):
        elm = arr[i]
        index = binary_search(arr, elm, 0, i - 1)
        arr[:] = arr[:index] + [elm] + arr[index:i] + arr[i + 1:]
    return arr


def binary_search(arr, elm, low, high):
    if low == high:
        if arr[low] > elm:
            return low
        else:
            return low + 1
    elif low > high:
        return low

    mid = (low + high) // 2
    if arr[mid] > elm:
        return binary_search(arr, elm, low, mid - 1)
    elif arr[mid] < elm:
        return binary_search(arr, elm, mid + 1, high)
    else:
        return mid


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
        input = """5 3 2 6 4 8 1 9 5"""
        output = """1 2 3 4 5 5 6 8 9"""
        self.assertIO(input, output)

    # def test_入力例_2(self):
    #     input = """3 5 2 6 4 8 1 9"""
    #     output = """1 2 3 4 5 6 8 9"""
    #     self.assertIO(input, output)

    # def test_入力例_3(self):
    #     input = """12 15"""
    #     output = """No"""
    #     self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
