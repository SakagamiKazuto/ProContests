from operator import itemgetter


def resolve():
    n = int(input())
    cs = []
    for _ in range(n):
        x, l = map(int, input().split())
        cs.append([x - l, x + l-1])

    coordinates = sorted(cs, key=itemgetter(1))

    now = coordinates[0][1]
    ans = 1
    for i in range(1, len(coordinates)):
        if coordinates[i][0] > now:
            now = coordinates[i][1]
            ans += 1
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
        input = """4
2 4
4 3
9 3
100 5"""
        output = """3"""
        self.assertIO(input, output)


    def test_入力例_2(self):
        input = """2
8 20
1 10"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
10 1
2 1
4 1
6 1
8 1"""
        output = """5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
