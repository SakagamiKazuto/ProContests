def resolve():
    input_list = input().split()
    m = int(input_list.pop(-1))

    hash_not_sorted = {}
    for input_str in input_list:
        k, v = map(str, input_str.split(":"))
        hash_not_sorted[int(k)] = v
    hash_sorted = sorted(hash_not_sorted.items())

    ans = ""
    for kv in hash_sorted:
        if m % kv[0] == 0:
            ans += kv[1]

    if ans == "":
        print(m)
    else:
        print(ans)

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
        input = """3:fizz 5:buzz 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3:hoge 5:fuga 3"""
        output = """hoge"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3:piyo 5:hogera 5"""
        output = """hogera"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """3:kabe 5:don 15"""
        output = """kabedon"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """5:hogera 3:piyo 2:huga 30"""
        output = """hugapiyohogera"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
