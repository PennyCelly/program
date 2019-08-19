"""
显示方式 意义
0        终端默认设置
1        高亮显示
4        使用下划线
5        闪烁
7       反白显示
8       不可见

前景色 背景色   颜色
30     40      黑色
31     41      红色
32     42      绿色
33     43      黃色
34     44      蓝色
35     45      紫红色
36     46      青蓝色
37     47      白色

语法格式：\033[显示方式;前景色;背景色m
"""
class bcolors:
    BLACK = '\033[1;30;m'
    RED = '\033[1;31;m'
    GREEN = '\033[1;32;m'
    YELLOW = '\033[1;33;m'
    BLUE =  '\033[1;34;m'

    def disable(self):
        self.BLACK = ''
        self.RED = ''
        self.BLUE = ''
        self.GREEN = ''
        self.YELLOW = ''
print(bcolors.YELLOW+"warning")



