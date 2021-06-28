import heapq


def resolve():
    Ai = []
    Bi = []
    pq = []

    n, k = map(int, input().split(" "))
    for _ in range(n):
        a, b = map(int, input().split(" "))
        Ai.append(a)
        Bi.append(b)

    for i in range(n):
        pq.append([Ai[i], Bi[i]])
    heapq.heapify(pq)

    ans = 0
    while k > 0:
        time, p_time = heapq.heappop(pq)
        k -= 1
        ans += time
        heapq.heappush(pq, [time + p_time, p_time])

    print(ans)

# これを↑に変えることでO(N×K)を節約出来る
# def resolve():
#     Ai = []
#     Bi = []
#     pq = []
#     heapq.heapify(pq)
#
#     n, k = map(int, input().split(" "))
#     for _ in range(n):
#         a, b = map(int, input().split(" "))
#         Ai.append(a)
#         Bi.append(b)
#
#     for i in range(n):
#         for j in range(1, k + 1):
#             heapq.heappush(pq, Ai[i] + (j - 1) * Bi[i])
#
#     ans = 0
#     for j in range(k):
#         ans += heapq.heappop(pq)
#     print(ans)


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
        input = """3 3
1 3
2 0
3 4"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 100000
22 59
26 60
72 72
47 3
97 16
75 41
82 77
17 97
32 32
28 7"""
        output = """7521307799"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 100000
1000000000 1000000000"""
        output = """5000050000000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
