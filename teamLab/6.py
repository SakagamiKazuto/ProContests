import collections


def resolve():
    l = []
    for i in range(2020, 2033):
        if i%4 == 0:
            l.append(i)


if __name__ == "__main__":
    resolve()
