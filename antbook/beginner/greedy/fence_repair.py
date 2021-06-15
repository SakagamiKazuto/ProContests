def resolve():
    n = int(input())
    L = list(map(int, input().split(" ")))
    sum = 0

    while n > 1:
        # 下から2つの値のindexを格納する
        mil1, mil2 = 0, 1
        if L[mil1] > L[mil2]:
            mil1, mil2 = mil2, mil1

        # mil1,2に確実に配列内の最小値2つが入ることを保証するため
        for i in range(2, n):
            if L[i] < L[mil1]:
                mil2 = mil1
                mil1 = i
            elif L[i] < L[mil2]:
                mil2 = i

        # 兄弟ノードの公式から
        node_sum = L[mil1] + L[mil2]
        sum += node_sum

        if mil1 == n - 1:
            mil1, mil2 = mil2, mil1

        # L[mil1,2]の既存値をノードの合計とその他で上書きすることで次のループでは"ひとつ上ノード"の処理を表現出来る
        L[mil1] = node_sum
        L[mil2] = L[n - 1]
        n -= 1
    print(sum)


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
        input = """3
8 5 8"""
        output = """34"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
