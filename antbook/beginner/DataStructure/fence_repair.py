import heapq
def resolve():
    n = int(input())
    L = list(map(int, input().split(" ")))
    sum = 0
    pq = []
    heapq.heapify(pq)
    for i in range(n):
        heapq.heappush(pq, L[i])

    while len(pq) > 1:
        l1 = heapq.heappop(pq)
        l2 = heapq.heappop(pq)
        sum += l1 + l2
        heapq.heappush(pq, l1 + l2)
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
