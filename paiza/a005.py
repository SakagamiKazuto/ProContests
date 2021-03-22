def resolve():
    a, b, n = map(int, input().split())
    pList = list(map(lambda x: int(x.replace("G", "0")), input().split()))
    i = 0
    point = 0
    frame = 1
    while i < n:
        if frame < a:
            if pList[i] == b:
                point += pList[i] + pList[i + 1] + pList[i + 2]
                i += 1
                frame += 1
            elif pList[i] + pList[i + 1] == b:
                point += pList[i] + pList[i + 1] + pList[i + 2]
                i += 2
                frame += 1
            else:
                point += pList[i] + pList[i + 1]
                i += 2
                frame += 1
        else:
            if pList[i] == b:
                if pList[i + 1] == b:
                    point += pList[i] + pList[i + 1] * 2 + pList[i + 2] * 3
                else:
                    point += pList[i] + (pList[i + 1] + pList[i + 2]) * 2
                break

            elif pList[i] + pList[i + 1] == b:
                point += pList[i] + pList[i + 1] + pList[i + 2] * 2
                break
            else:
                point += pList[i] + pList[i + 1]
                break
    print(point)



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
        input = """10 10 18
3 4 G 1 8 2 6 2 10 2 7 G 10 10 10 9 1 3"""
        output = """145"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """15 5 24
5 5 5 4 G 1 G 5 3 2 1 4 4 G G 1 5 5 5 2 1 5 3 1"""
        output = """124"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """15 5 24
5 5 5 4 G 1 G 5 3 2 1 4 4 G G 1 5 5 5 2 1 5 5 5"""
        output = """141"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """1 1 3
1 1 1"""
        output = """6"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
