# !/usr/bin/python3

# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a = 0
b = 1
while b < 50:
    print(b)
    a = a + b
    b = a + b
    print(a)

# 示例
a, b = 0, 1                     # 复合赋值
while b < 50:
    print(b)
    a, b = b, a + b             # 同样为复合赋值：先计算a + b,再将b的值赋给a，a + b 的值赋给b

# end关键字：1.用于将输出结果输出到同一行 2.可以在输出的末尾添加不同字符
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a + b
