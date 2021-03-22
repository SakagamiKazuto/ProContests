def resolve():
    n = int(input())
    normalList = []
    abnomalList = []
    for i in range(n):
        s = input()
        if s[0] == "!":
            # あらかじめ!を抜いておく
            abnomalList.append(s[1:])
        else:
            normalList.append(s)
    abnomalList = set(abnomalList)
    normalList = set(normalList)

    for nl in normalList:
        if nl in abnomalList:
            print(nl)
            return

    # n <=10^5ゆえにここでTLE
    # for s1 in normalList:
    #     for s2 in abnomalList:
    #         if "!" + s1 == s2:
    #             print(s1)
    #             return
    print("satisfiable")


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
        input = """6
a
!a
b
!c
d
!d"""
        output = """a"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10
red
red
red
!orange
yellow
!blue
cyan
!green
brown
!gray"""
        output = """satisfiable"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
