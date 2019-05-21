"""
----------------------------while 循环语句-------------------------------
"""
# 计算1到100总和
m = 0
n = 1
while n != 101:
    m += n
    n += 1
print(m)

# 无线循环
# var = 1
# while var == 1:  # 表达式永远为 true
#     num = int(input("输入一个数字  :"))
#     print("你输入的数字是: ", num)
#
# print("Good bye!")

# while 循环使用else语句
count = 0
while count < 9:
    print(count, '小于9')
    count += 1
else:
    print(count, '不比9小')


# 简单语句组
m = 1
n = True
while (m == n):print('it\'s true')      # 如果while循环体中只有一条语句，你可以将该语句与while写在同一行中


