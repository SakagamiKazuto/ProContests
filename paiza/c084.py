def resolve():
    s = input()
    sLen = len(s)
    wrapper = "+" * (sLen + 2)
    print("{0}\n+{1}+\n{0}".format(wrapper, s))


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
        input = """paiza"""
        output = """+++++++
+paiza+
+++++++"""
        self.assertIO(input, output)

    # def test_入力例_2(self):
    #     input = """19"""
    #     output = """290"""
    #     self.assertIO(input, output)
    #
    # def test_入力例_3(self):
    #     input = """1"""
    #     output = """110"""
    #     self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
