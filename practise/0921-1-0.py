"""
寻找第n个默尼森数
"""


def prime(num):
    flag = True
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break
    return flag


def monisen(no):
    n = 1
    mo = ''
    k = 2
    while n <= no:
        if prime(k):
            mo = pow(2, k) - 1
            if prime(mo):
                n += 1
        k += 1
    return mo


print(monisen(int(input())))