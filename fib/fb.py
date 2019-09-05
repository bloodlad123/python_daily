"""实现输出斐波那契数列"""


def fb(x):
    a = 1
    b = 1
    while x > 0:
        yield a
        a, b = b, a+b
        x -= 1


def main():
    for x in fb(5):
        print(x, end="\t")


if __name__ == '__main__':
    main()