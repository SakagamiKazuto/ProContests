def dfs(n, ans):
    if n <= 1:
        return n

    ans += n + dfs(n - 1, ans)
    return ans


def resolve():
    print(dfs(int(input()), 0))


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
        input = """5"""
        output = """15"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
