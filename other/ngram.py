s = ""
n = 0
ngram = set()


def rec(i, sn):
    # ベースケース
    if i == n:
        ngram.add(sn)
        return

    # 再帰ステップ
    rec(i + 1, sn + s[i])
    rec(i + 1, sn)


def resolve():
    global s, n
    s = input()
    n = len(s)
    rec(0, "")
    print(sorted(list(ngram)))


# def resolve():
#     s = input()
#     n = len(s) + 1
#     ans = []
#     for i in range(1, n):
#         # 始点なのでn-1でいい
#         for j in range(n - i):
#             # これだとnode_depthが増えたときに対応できない→再帰
#             ans.append(''.join(s[j:j + i]))
#     print(ans)


# if __name__ == "__main__":
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
        input = """abc"""
        output = """['', 'a', 'ab', 'abc', 'ac', 'b', 'bc', 'c']"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """abcd"""
        output = """['', 'a', 'ab', 'abc', 'abcd', 'abd', 'ac', 'acd', 'ad', 'b', 'bc', 'bcd', 'bd', 'c', 'cd', 'd']"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
