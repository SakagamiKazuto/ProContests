def resolve():
    n = int(input())
    Alist = list(map(int, input().split()))
    Adict = {}
    for a in Alist:
        if a not in Adict:
            Adict[a] = 0
        Adict[a] += 1
    for i in range(1, n + 1):
        if i not in Adict:
            print(0)
        else:
            print(Adict[i])

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
        input = """5
1 1 2 2"""
        output = """2
2
0
0
0"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10
1 1 1 1 1 1 1 1 1"""
        output = """9
0
0
0
0
0
0
0
0
0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7
1 2 3 4 5 6"""
        output = """1
1
1
1
1
1
0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
