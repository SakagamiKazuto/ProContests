def resolve():
    s = input()
    slist1 = []
    slist2 = []
    slist3 = []
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            slist1.append(s[i:i+1] + s[j:])
            slist2.append(s[i:i+1] + s[j:(len(s))-j])
            slist3.append(s[i:i+1] + s[j:j+1])

    ans = set(slist1 + slist2 + slist3)
    sortAns = sorted(list(ans))
    # print(sortAns)
    print(len(sortAns))


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

    # def test_入力例_0(self):
    #     input = """abc"""
    #     output = """7"""
    #     self.assertIO(input, output)

    def test_入力例_1(self):
        input = """abcd"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """abcde"""
        output = """27"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """robot"""
        output = """27"""
        self.assertIO(input, output)



if __name__ == "__main__":
    unittest.main()
