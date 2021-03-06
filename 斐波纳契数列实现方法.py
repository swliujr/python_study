# coding:utf-8


# 用for循环的方法，改进为列表解析
def fib(n):
    if n == 1:
        return [0]
    else:
        lst = [0, 1]
        [lst.append(lst[-1] + lst[-2]) for i in range(n - 2)]
        return lst


print(fib(10))


# 用迭代器的方法
class Fibs:
    def __init__(self, maxi):
        self.maxi = maxi
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        fi = self.a
        if fi > self.maxi:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fi


fibs = Fibs(100000)
fib_lst = [next(fibs) for i in range(15)]
print(fib_lst)


# 用递归的方法，Python不建议使用递归，可能会有死循环
def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


fibo_lst = [fibo(i) for i in range(20)]
print(fibo_lst)


# 用while循环的方法
def fibona(n):
    a, b = 0, 1
    i = 1
    result = []
    while i <= n:
        result.append(a)
        a, b = b, a + b
        i += 1
    return result


print(fibona(25))


# 用生成器的方式
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


import itertools
print(list(itertools.islice(fibonacci(), 30)))

# 用矩阵的方式
import numpy as np
def func(n):
    F = np.mat([[1, 1], [1, 0]])
    return pow(F, n-1)[0, 0]


print([func(i) for i in range(30)])
