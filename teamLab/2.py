def resolve():
    num = 1234567890
    sumn = 0
    for i in range(1, 1234567891):
        if num % i == 0:
            if i <= 10000000:
                print("THROUGH")
                sumn += i

    print("FAFAFA")
    print(sumn)


if __name__ == "__main__":
    resolve()

# import sys
# from io import StringIO
# import unittest
#
#
# class TestClass(unittest.TestCase):
#     def assertIO(self, input, output):
#         stdout, stdin = sys.stdout, sys.stdin
#         sys.stdout, sys.stdin = StringIO(), StringIO(input)
#         resolve()
#         sys.stdout.seek(0)
#         out = sys.stdout.read()[:-1]
#         sys.stdout, sys.stdin = stdout, stdin
#         self.assertEqual(out, output)
#
#     def test_入力例_1(self):
#         input = """3 5"""
#         output = """Yes"""
#         self.assertIO(input, output)
#
#     def test_入力例_2(self):
#         input = """16 2"""
#         output = """No"""
#         self.assertIO(input, output)
#
#     def test_入力例_3(self):
#         input = """12 15"""
#         output = """No"""
#         self.assertIO(input, output)
#
#
# if __name__ == "__main__":
#     unittest.main()
