"""
条件控制
1.if-elif-else
2.每个条件后面都要使用冒号：
3.用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块
常用操作运算符
1.<	                                   小于
2.<=	                                   小于或等于
3.>	                                   大于
4.>=	                                   大于或等于
5.==	                                   等于，比较两个值是否相等
6.!=	                                   不等于
"""
# 猜数字游戏
# num = 43
# num_input = -1
# print("猜数字游戏")
# while num_input != num:
#     num_input = int(input("请输入你猜的数字："))
#     if num_input < num:
#         print("猜的数字太小了。。。")
#     elif num_input > num:
#         print("猜的数字太大了。。。")
#     elif num_input == num:
#         print("你猜对啦！")
# # 退出提示
# input("点击enter键退出")

"""
条件嵌套使用
"""
status = -1                                      # 用户输入额度
static_status = 5                                # 授信成功
sign = -1
static_sign_used = 0                             # 额度已使用
static_sign_unuse = 1                            # 额度未使用
static_sign_out = 2                              # 额度失效
tip_end = 'end'
tip_in = ''
while tip_in != tip_end:
    status = int(input("输入授信status："))
    if status == static_status:
        sign = int(input("输入额度sign："))
        if sign == static_sign_unuse:
            print("您已授信成功且额度未使用\r\n")
        elif sign == static_sign_used:
            print("您授信成功但已使用\r\n")
        elif sign == static_sign_out:
            print("您已授信成功但已失效\r\n")
    elif status != static_status:
        print("您未授信！\r\n")
    tip_in = str(input("输入end结束程序,按其他键继续\r\n"))



