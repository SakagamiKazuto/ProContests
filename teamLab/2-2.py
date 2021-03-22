def resolve():
    num = 1234567890
    divisors = []
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            divisors.append(i)
            if i != num // i:
                divisors.append(num // i)

    # divisors.sort()
    list2 = list(filter(lambda x: x <= 10000000, divisors))

    # print("DADA")
    print(sum(list2))


if __name__ == "__main__":
    resolve()
