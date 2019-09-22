"""
寻找n以内的亲密数对
"""


def fac(n):
    list1 = []
    for m in range(1, n):
        if n % m == 0:
            list1.append(m)
    return sum(list1)


def main():
    flag = True
    n = int(input())
    for i in range(1, n + 1):
        si = fac(i)
        for j in range(1, n + 1):
            if si == j:
                sj = fac(j)
                if sj == i and i != j and i < j:
                    flag = False
                    print("{}-{}".format(i, j), end="\t")

    if flag:
        print("n以内不存在亲密数对！")


if __name__ == "__main__":
    main()
































