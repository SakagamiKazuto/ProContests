def resolve():
    n = int(input())
    key_by_ini0 = {}
    # 構造体の初期化
    for i in range(n):
        ini0, ini1 = map(int, input().split())
        if ini0 not in key_by_ini0:
            key_by_ini0[ini0] = []
        key_by_ini0[ini0].append([ini0, ini1])

    # カウント処理
    count = 0
    for k in key_by_ini0.keys():
        del_list = []
        for L01 in key_by_ini0[k]:
            revL01 = [L01[1], L01[0]]
            try:
                if revL01 in key_by_ini0[revL01[0]]:
                    count += 1
                    key_by_ini0[revL01[0]].remove(revL01)
                    del_list.append(L01)
            except:
                pass
        for dl in del_list:
            key_by_ini0[k].remove(dl)

    print(count)

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

#     def test_入力例_同じ場合(self):
#         input = """4
# 1 1
# 1 1
# 1 1
# 1 1"""
#         output = """2"""
#         self.assertIO(input, output)

#     def test_入力例_1(self):
#         input = """3
# 1 2
# 2 3
# 2 1"""
#         output = """1"""
#         self.assertIO(input, output)

#     def test_入力例_2(self):
#         input = """3
# 1 2
# 2 1
# 2 1"""
#         output = """1"""
#         self.assertIO(input, output)

#     def test_入力例_debug_main(self):
#         input = """18
# 1 2
# 1 2
# 1 2
# 1 2
# 1 2
# 1 2
# 1 2
# 1 2
# 1 2
# 1 2
# 2 1
# 2 1
# 2 1
# 2 1
# 2 1
# 2 1
# 2 1
# 2 1
# """
#         output = """8"""
#         self.assertIO(input, output)

    def test_入力例_debug_main(self):
        input = """18
69 77
77 69
77 69
77 69
69 77
77 69
69 77
77 69
69 77
77 69
69 77
69 77
69 77
69 77
77 69
77 69
77 69
77 69"""
        output = """8"""
        self.assertIO(input, output)

#     def test_入力例_3(self):
#         input = """46
# 76 29
# 69 77
# 29 76
# 96 21
# 77 69
# 54 36
# 76 29
# 76 29
# 99 5
# 77 69
# 5 99
# 76 29
# 99 5
# 54 36
# 29 76
# 21 96
# 76 29
# 76 29
# 77 69
# 69 77
# 77 69
# 54 36
# 36 54
# 36 54
# 69 77
# 77 69
# 29 76
# 54 36
# 76 29
# 76 29
# 69 77
# 77 69
# 54 36
# 69 77
# 36 54
# 69 77
# 76 29
# 69 77
# 69 77
# 77 69
# 29 76
# 77 69
# 29 76
# 77 69
# 77 69
# 54 36"""
#         output = """18"""
#         self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
