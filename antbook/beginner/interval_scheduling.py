# 重複が許されない時間単位の中で、できるだけ多くのタスクを取る
def resolve():
    n = int(input())
    s = list(map(int, input().split(" ")))
    t = list(map(int, input().split(" ")))
    # for sorted(): ending=itv[0], start=itv[1]
    itv = []
    for i in range(n):
        itv.append([t[i], s[i]])
    sorted(itv)

    ans = 0
    tmp = 0
    for i in range(n):
        if itv[i][1] > tmp:
            ans += 1
            tmp = itv[i][0]
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
        input = """5
1 2 4 6 8
3 5 7 9 10"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
