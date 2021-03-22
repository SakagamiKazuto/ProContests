def resolve():
    n, m, t = map(int, input().split())
    ab = []
    for _ in range(m):
        ab.append(list(map(int, input().split())))
    additions = [n]
    subtractions = [ab[0][0]]
    # abの中身を探査して、addtionsとsubtractionsに値を入れていく
    for i in range(m):
        additions.append(ab[i][1] - ab[i][0])
    for i in range(m - 1):
        subtractions.append(ab[i + 1][0] - ab[i][1])
    subtractions.append(t - ab[m - 1][1])

    # sum
    now = 0
    for i in range(len(additions)):
        add = additions[i] + now
        if add >= n:
            add = n

        now = add - subtractions[i]
        if now <= 0:
            print("No")
            return
    print("Yes")



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

    def test_入力例_1(self):
        input = """10 2 20
9 11
13 17"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 2 20
9 11
13 16"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """15 3 30
5 8
15 17
24 27"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """20 1 30
20 29"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """20 1 30
1 10"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
