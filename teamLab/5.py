import collections


def resolve():
    l = []
    for i in range(0, 51):
        for j in range(0, 41):
            for k in range(0, 31):
                l.append(i*30 + j*82 + k*205)

    print(len(list(set(l))))


if __name__ == "__main__":
    resolve()
