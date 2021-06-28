def setup_value(n, keys):
    di = {}
    for i in range(n):
        s = input()
        keys.add(s)
        if s not in di:
            di[s] = 1
        else:
            di[s] += 1
    return di, keys


def resolve():
    keys = set()
    n = int(input())
    dn, keys = setup_value(n, keys)
    m = int(input())
    dm, keys = setup_value(m, keys)


    ans = 0
    for k in keys:
        if k not in dn:
            dn[k] = 0
        if k not in dm:
            dm[k] = 0

        x = dn[k] - dm[k]
        if ans < x:
            ans = x

    print(ans)

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

    def test_入力例_1(self):
        input = """3
apple
orange
apple
1
grape"""
        output = """2"""
        self.assertIO(input, output)

#     def test_入力例_2(self):
#         input = """3
# apple
# orange
# apple
# 5
# apple
# apple
# apple
# apple
# apple"""
#         output = """1"""
#         self.assertIO(input, output)
#
#     def test_入力例_3(self):
#         input = """1
# voldemort
# 10
# voldemort
# voldemort
# voldemort
# voldemort
# voldemort
# voldemort
# voldemort
# voldemort
# voldemort
# voldemort"""
#         output = """0"""
#         self.assertIO(input, output)
#
#     def test_入力例_4(self):
#         input = """6
# red
# red
# blue
# yellow
# yellow
# red
# 5
# red
# red
# yellow
# green
# blue"""
#         output = """1"""
#         self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
