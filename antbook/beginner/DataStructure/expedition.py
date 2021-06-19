import heapq


def resolve():
    n = int(input())
    l = int(input())
    p = int(input())
    a = list(map(int, input().split(" ")))
    b = list(map(int, input().split(" ")))
    pq = []
    heapq.heapify(pq)

    ans = 0
    pos = 0
    tank = p
    for i in range(n):
        distance = a[i] - pos

        # 「今タンクにある量 < 次進む距離」ならその分燃料補強したい
        while tank - distance < 0:
            if len(pq) == 0:
                print(-1)
                return
            tank += heapq.heappop(pq)
            ans += 1

        # タンクに十分量入ってるのは保証されているので移動時の処理を行う
        tank -= distance
        pos = a[i]
        heapq.heappush(pq, b[i])
    print(ans)


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
        input = """4
25
10
10 14 20 21
10 5 2 4"""
        output = """2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
