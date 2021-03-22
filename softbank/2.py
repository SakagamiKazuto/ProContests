import itertools


def resolve():
    n, m, k = map(int, input().split())
    orig_list = []
    for i in range(n):
        orig_list.append(list(input()))

    blist = sorted(getBlist(orig_list, n, m))
    noblist = sorted(getNoBList(orig_list, blist, n, m))
    swaped_list = swapEachList(noblist, blist, n, m, k)
    if len(swaped_list) == 0:
        print(0)
    else:
        print(sum(list(map(int, swaped_list))))


# noblistの下とblistの上をk個分値を交換する
def swapEachList(noblist, blist, n, m, k):
    if len(blist) == 0:
        return noblist

    if k >= len(noblist):
        k = len(noblist)

    for i in range(1, k + 1):
        noblist.extend(blist.pop(-i))
        noblist.pop(0)
    return noblist


def getBlist(orig_list, n, m):
    blist = []
    inserted_row = set()
    inserted_column = set()
    for i in range(n):
        for j in range(m):
            if orig_list[i][j] == "B":
                if j not in inserted_column:
                    blist.extend(getColumnList(i, j, m, n, orig_list))
                    inserted_column.add(j)

                if i not in inserted_row:
                    blist.extend(getRowList(i, j, m, n, orig_list))
                    inserted_row.add(i)
    return blist


# origからblistをremoveして"B"も抜くことで生成する
def getNoBList(orig_list, blist, n, m):
    orig_list = list(itertools.chain.from_iterable(orig_list))
    for v in blist:
        orig_list.remove(v)
    noblist = [item for item in orig_list if item != "B"]
    return noblist


# Bが存在する行列を格納するのが目的
# i→n, j→mとなりループで利用される
def getColumnList(i, j, m, n, orig_list):
    blist = []
    # 縦を入れる
    for i2 in range(n):
        if orig_list[i2][j] != "B":
            blist.append(orig_list[i2][j])
    return blist


def getRowList(i, j, m, n, orig_list):
    blist = []
    # 横の値を入れる
    for j2 in range(m):
        if orig_list[i][j2] != "B":
            blist.append(orig_list[i][j2])
    return blist


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

#         def test_入力例_1(self):
#             input = """3 5 0
# B8B3B
# 53243
# 32452"""
#             output = """14"""
#             self.assertIO(input, output)

#     def test_入力例_2(self):
#         input = """3 5 1
# B8B3B
# 53243
# 32452"""
#         output = """20"""
#         self.assertIO(input, output)


#     def test_入力例_all_B1(self):
#         input = """1 1 1000
# B"""
#         output = """0"""
#         self.assertIO(input, output)

#     def test_入力例_all_B2(self):
#         input = """1 1 1000
# 8"""
#         output = """8"""
#         self.assertIO(input, output)

    def test_入力例_all_B3(self):
        input = """2 2 0
B3
4B"""
        output = """0"""
        self.assertIO(input, output)

    # def test_入力例_2(self):
    #     input = """3:hoge 5:fuga 3"""
    #     output = """hoge"""
    #     self.assertIO(input, output)
    #
    # def test_入力例_3(self):
    #     input = """3:piyo 5:hogera 5"""
    #     output = """hogera"""
    #     self.assertIO(input, output)
    #
    # def test_入力例_4(self):
    #     input = """3:kabe 5:don 15"""
    #     output = """kabedon"""
    #     self.assertIO(input, output)
    #
    # def test_入力例_5(self):
    #     input = """5:hogera 3:piyo 2:huga 30"""
    #     output = """hugapiyohogera"""
    #     self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
