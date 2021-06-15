def resolve():
    n = int(input())
    s = str(input())
    ans = ""
    left, right = 0, n - 1

    while left <= right:
        is_left = False
        for i in range(right - left + 1):  # i <= right-leftで動くように
            if s[left + i] < s[right - i]:
                is_left = True
                break
            elif s[left + i] > s[right - i]:
                is_left = False
                break
        if is_left:
            ans += s[left]
            left += 1
        else:
            ans += s[right]
            right -= 1

    print(ans)


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
        input = """6
ACDBCB"""
        output = """ABCBCD"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
