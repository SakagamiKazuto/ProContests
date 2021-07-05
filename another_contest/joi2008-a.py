def resolve():
    n = 1000 - int(input())
    coins = [500, 100, 50, 10, 5, 1]
    ans = 0
    for c in coins:
        x = n // c
        n -= c * x
        ans += x
    print(ans)


if __name__ == "__main__":
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
        input = """380"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1"""
        output = """15"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
