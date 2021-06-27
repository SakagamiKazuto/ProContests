def resolve():
    s2 = input()
    t = input()
    N = len(s2)
    tn = len(t)

    s = s2
    flag = False
    # Tの有無判定
    for n in range(N, tn - 1, -1):
        x = s2[n - tn:n]
        b = all([x[i] == t[i] or x[i] == "?" for i in range(len(x))])
        if b:
            s = s2[:n - tn] + t + s2[n:]
            s = s.replace('?', 'a')
            flag = True
            break

    if flag:
        print(s)
    else:
        print("UNRESTORABLE")


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
#         input = """?tc????
# coder"""
#         output = """atcoder"""
#         self.assertIO(input, output)

    def test_入力例_3(self):
        input = """?c????a
coder"""
        output = """acodera"""
        self.assertIO(input, output)

#     def test_入力例_2(self):
#         input = """??p??d??
# abc"""
#         output = """UNRESTORABLE"""
#         self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
