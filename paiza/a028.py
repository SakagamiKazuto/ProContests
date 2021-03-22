# 実装の方針が見えず例をトレースしたが通らなかった
# テストケース洗い出さないと無理そう
def resolve():
    S, P = map(int, input().split())
    ansList = []
    for i in range(P):
        v = int(S * ((1.01) ** i))
        v = int(v * ((100 + (P - i)) / 100))
        ansList.append(v)

    print(max(ansList))


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
        input = """10000 3"""
        output = """10303"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 10"""
        output = """11"""
        self.assertIO(input, output)

    def test_境界値(self):
        input = """1000000000 1000"""
        output = """20959155637813"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
