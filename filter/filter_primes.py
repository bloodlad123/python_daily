"""
使用filter求素数
"""
# 生成一个从3开始的奇数无限序列


def odd():
    n = 1
    while True:
        n += 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0
# def _not_divisible(n):
#     def f(x):
#         return x % n > 0
#     return f


def primes():
    yield 2
    init_num = odd()  # 初始序列
    while True:
        n = next(init_num)  # 返回序列的第一个数字
        yield n
        init_num = filter(_not_divisible(n), init_num)


res = []
for i in primes():
    if i < 100:
        res.append(i)
    else:
        break
print(res) 