def resolve():
    s = list(map(int, input()))
    s.sort()
    # 0ではない一番小さな値を特定した上で、
    minNotZero = min(filter(lambda x: x >= 1, s))
    # 1つlistから"特定した値を削除する"
    s.remove(minNotZero)
    # その値をsの先頭に入れ、
    s.insert(0, minNotZero)
    print(''.join(list(map(str, s))))


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
        input = """201"""
        output = """102"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """12212122212222"""
        output = """11112222222222"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
