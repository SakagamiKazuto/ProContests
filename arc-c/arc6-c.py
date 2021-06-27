def resolve():
    n = int(input())
    X = [int(input()) for _ in range(n)]

    bucket = []
    for x in X:
        # len() + 1することで"適切なtopが存在しない" or "道半ば"を状態管理
        for i in range(len(bucket) + 1):
            if i == len(bucket):
                bucket.append(x)
            if x <= bucket[i]:
                bucket[i] = x
                break
    print(len(bucket))


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

    #     def test_入力例_1(self):
    #         input = """5
    # 4
    # 3
    # 1
    # 2
    # 1"""
    #         output = """2"""
    #         self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7
93
249
150
958
442
391
25"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4
100
100
100
100"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """6
5
10
15
20
25
30"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """15
3
1
4
1
5
9
2
6
5
3
5
8
9
7
9"""
        output = """6"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
