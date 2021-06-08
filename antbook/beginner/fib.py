def resolve():
    print(fib(int(input())))

# fib is
# an = an-1 + an-2 && a1=1, a0=0
def fib(i):
    if i <= 1:
        return i
    return fib(i-1) + fib(i-2)

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
        input = """5"""
        output = """5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
