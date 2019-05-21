"""
标识符
#由  字母、 数字、下划线  组成，开头必须是字母或者_
#不能以数字开头
#区分大小写
#以下划线开头的标识符是有特殊意义的。
###以单下划线开头 _foo 的代表 不能直接访问的类属性，需通过 类提供的接口 进行访问，不能用 from xxx import * 而导入。
###以双下划线开头的 __foo 代表 类的私有成员，以双下划线开头和结尾的 __foo__ 代表 Python 里特殊方法专用的标识，如 __init__() 代表类的构造函数。
"""

centens='''
多行语句
一般以新行作为语句的结束符
使用斜杠（ \）将一行的语句分为多行显示
语句中包含 [], {} 或 () 括号就不需要使用多行连接符
'''

'''
#word = 'word'
#sentence = "这是一个句子。"
#paragraph = """这是一个段落。
'''
'''
等待用户输入: input("按下 enter 键退出，其他任意键显示...\n");
'''

days = ['Monday', 'Tuseday', 'Wednesday', 'Thursday', 'Friday', ' Saturday', 'Sunday']
ganxie = '感谢'
shiyogn = '使用'
print(days)
print(centens)
input("按下 enter 键退出，其他任意键显示...\n")
print(ganxie, shiyogn)

print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义





