# -*- coding:utf-8 -*-
"""
生成杨辉三角
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
[1, 5, 10, 10, 5, 1]
[1, 6, 15, 20, 15, 6, 1]
[1, 7, 21, 35, 35, 21, 7, 1]
[1, 8, 28, 56, 70, 56, 28, 8, 1]
[1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
"""


# def triangles():
#     list1 = [1]
#     while True:
#         yield list1
#         list1 = [sum(i) for i in zip([0] + list1, list1 + [0])]


def triangles():
    list1 = []
    while True:
        for i in range(1, len(list1)):
            list1[-i] = list1[-i - 1] + list1[-i]
        list1.append(1)
        yield list1[:]


def main():
    n = 0
    result = []
    for i in triangles():
        result.append(i)
        n += 1
        if n == 10:
            break
    for j in result:
        print(j)


if __name__ == '__main__':
    main()
