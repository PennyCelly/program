'''比较运算符'''
print("------算数运算符---------")
a = 13
b = 7
print(a + b)       # a加b
print(b - a)       # b减a
print(a * b)       # a乘b
print(a / b)       # a除以b
print(a % b)       # a除以b,取余====取模
print(a // b)      # a除以b，取商，向下取接近除数的整数
print(a**b, '\n')        # a的b次幂


'''比较运算符'''
print("------比较运算符---------")
print(a == b)      #a等于b
print(a != b)      #a不等于b
print(a > b)
print(a < b)
print(a >= b)
print(a <= b,'\n')


'''复制运算符'''
print("------复制运算符---------")
q = a
print(q)
q += a
print(q)
q -= a
print(q)
q /= a
print(q)
q *= a
print(q)
q %= a
print(q)
q //= a
print(q)
q **= a
print(q)


print("------位运算符---------")
a = 60  # 0011 1100
b = 13  # 0000 1101
c = 0
c1 = a & b      # 与--都为1，才是1
c2 = a | b      # 或--有一个是1，就为1
c3 = a ^ b      # 异或--不同为1，相同为0
c4 = ~a         # 按位取反
c5 = a << 2     # 向左移位，用0补齐
c6 = a >> 2     # 向右移位，用0补齐
print(c1, c2, c3, c4, c5, c6, '\n')

print("------逻辑运算符---------")
a = 10
b = 20
c1 = a and b         # "与---都为真才是真，有一个假则都是假"①x 为 False，返回 False，②x是True，否则它返回 y 的计算值。
c2 = a or b          # "或---有一个真就为真" ① x 是 True，返回 x 的值，②x是False，返回 y 的计算值。
c3 = not a           # 非
c4 = not a and b
print(c1, c2, c3, c4, '\n')

print("------成员运算符---------")
a = 10
b = 20
c = "20304"
str1 = "102030405060607008"
list1 = [10, '20', '30']
if a in list1:
    print('true')                    # 注意元素类型
else:
    print('false')


if c not in str1:
    print('true')                    # 注意元素类型,在字符串中只能判断字符串
else:
    print('false')

print("------身份运算符---------")
# is 是判断两个标识符是不是引用自一个对象
# s 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等
a = 20
b = 20
c = 30
d = 'abcdefdg'
e = ['abcdefdg']
if a is b:
    print('a和b有相同标识')
if a is not c:
    print('a和c有不同标识')
if d is e:
    print("d和e有相同标识")                # 元素类型不同，所以是不同标识
else:
    print("d和e没有相同标识")
if d == e:
    print("d和e有相同变量值")  # 元素类型不同，所以是不同标识
else:
    print("d和e有相同变量值")

print("------运算符优先级---------")
'''
**                         指数优先级最高
~ + -                      按位翻转，一元加号，减号 (最后两个的方法名为 +@ 和 -@)
* / % //                   乘 除 取模 取整数除
+ -                        加减
>>  <<                     右移，左移
&                          位与
^ |                        位运算符
<= <  >  >=                比较运算符
< > == !=                  等于运算符
= %= /= //= -= += *= **=   赋值运算符
is is not                  身份运算符
in not in                  成员运算符
and or not                  逻辑运算符【not 优先于 and 优先于 or】
'''
