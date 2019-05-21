"""
生成器
1.使用了 yield 的函数被称为生成器（generator）
2.生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器
3.在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。
"""
import sys


def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a+b
        counter += 1


f = fibonacci(10)
while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()
