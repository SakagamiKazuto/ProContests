def resolve():
    n = int(input())
    print(100 + n*10)


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
        input = """3"""
        output = """130"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """19"""
        output = """290"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1"""
        output = """110"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
