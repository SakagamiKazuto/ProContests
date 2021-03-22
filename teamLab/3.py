def resolve():
    for i in range(90000, 1000000):
        sumi = 0
        for j in range(1, i + 1):
            sumi += 1 / j
        print(sumi)
        if sumi >= 12:
            print(i)
            break


if __name__ == "__main__":
    resolve()
