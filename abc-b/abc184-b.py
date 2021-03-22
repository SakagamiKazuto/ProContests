# 手元では通るのに本番では失敗した
def resolve():
    n, x = map(int, input().split())
    S = input()
    now = x
    for s in S:
        if (s == 'o'):
            now += 1
        elif now > 0:
            now -= 1

    print(now)

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
        input = """3 0
xox"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """20 199999
oooooooooxoooooooooo"""
        output = """200017"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """20 10
xxxxxxxxxxxxxxxxxxxx"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
