def resolve():
    s = input()
    n = len(s) + 1
    ans = []
    for i in range(1, n):
        for j in range(n - i):
            ans.append(''.join(s[j:j + i]))
    print(ans)


# if __name__ == "__main__":
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
        input = """abc"""
        output = """['a', 'b', 'c', 'ab', 'bc', 'abc']"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
