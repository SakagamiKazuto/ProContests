from operator import itemgetter


def resolve():
    N, M = map(int, input().split(" "))
    ab = sorted([tuple(map(int, input().split())) for _ in range(M)], key=itemgetter(1))

    removed = -1
    ans = 0
    for a, b in ab:
        # bi < ajな区間をあぶり出す
        if a > removed:
            removed = b - 1
            ans += 1
    print(ans)


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
        input = """5 2
1 4
2 5"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """9 5
1 8
2 7
3 5
4 6
7 9"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 10
1 2
1 3
1 4
1 5
2 3
2 4
2 5
3 4
3 5
4 5"""
        output = """4"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
