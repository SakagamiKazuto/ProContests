def resolve():
    X, Y = map(int, input().split(" "))
    now = X
    ans = 1
    while True:
        if 2 * now <= Y:
            ans += 1
            now *= 2
        else:
            break
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
        input = """3 20"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """25 100"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """314159265 358979323846264338"""
        output = """31"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
