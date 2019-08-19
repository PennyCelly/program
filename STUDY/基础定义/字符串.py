# !/usr/bin/python3
# 一、访问字符串中的值
var1 = 'Hello World!'
var2 = "Runoob"

print("var1[0]: ", var1[0])
print("var2[1:5]: ", var2[1:5])

# 二、字符串更新
var3 = 'Hello Python!'
print('piupiu' + var3[5:-1])

# 三、转义字符

# \(在行尾时)	续行符
# \\	        反斜杠符号
# \'	        单引号
# \"	        双引号
# \a	        响铃
# \b	        退格(Backspace)
# \e	        转义
# \000	    空
# \n	        换行
# \v	        纵向制表符
# \t	        横向制表符
# \r	        回车
# \f	        换页
# \oyy	    八进制数，yy代表的字符，例如：\o12代表换行
# \xyy	    十六进制数，yy代表的字符，例如：\x0a代表换行
# \other	    其它的字符以普通格式输出
print('Hello\
      world')

# 四、字符串运算符
"""
+	             字符串连接
*	             重复输出字符串	
[]	             通过索引获取字符串中字符
[ : ]	         截取字符串中的一部分，遵循左闭右开原则，str[0,2] 是不包含第 3 个字符的。l
in	             成员运算符 - 如果字符串中包含给定的字符返回 True	
not in	         成员运算符 - 如果字符串中不包含给定的字符返回 True	
r/R	             原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 原始字符串除在字符串的第一个引号前加上字母 r（可以大小写）以外，与普通字符串有着几乎完全相同的语法。	
%	             格式字符串
"""
a = "I'm learning Python by myself!"
b = "I must hold on!"
print(a + b)
print(b * 3)
print(a[5])
print(a[:9])
if r"I'm" in a:
    print("I'm in")
print(r'\n')
print(R'\n')

# 五、字符串格式化
"""
1.作用：Python 支持格式化字符串的输出 。尽管这样可能会用到非常复杂的表达式，但最基本的用法是将一个值插入到一个有字符串格式符 %s 的字符串中。
2.    %c	 格式化字符及其ASCII码
      %s	 格式化字符串
      %d	 格式化整数
      %u	 格式化无符号整型
      %o	 格式化无符号八进制数
      %x	 格式化无符号十六进制数
      %X	 格式化无符号十六进制数（大写）
      %f	 格式化浮点数字，可指定小数点后的精度
      %e	 用科学计数法格式化浮点数
      %E	 作用同%e，用科学计数法格式化浮点数
      %g	 %f和%e的简写
      %G	 %f 和 %E 的简写
      %p	 用十六进制数格式化变量的地址
"""
print("hello, %s ! my phonenumber is %d " % ('Sally', 13896431356))    #注意括号使用 print（'xxx %d xxx %s'%(xx,xx)）
"""
3.格式化操作符辅助指令
      *	     定义宽度或者小数点精度
      -	     用做左对齐
      +	     在正数前面显示加号( + )
      <sp>	     在正数前面显示空格
      #	     在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'(取决于用的是'x'还是'X')
      0	     显示的数字前面填充'0'而不是默认的空格
      %	     '%%'输出一个单一的'%'
     (var)	 映射变量(字典参数)
      m.n.	 m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话)
    Python2.6 开始，新增了一种格式化字符串的函数 str.format()，它增强了字符串格式化的功能。
"""

# 六、三引号
# python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符
para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print(para_str)

# 七、Unicode字符串
"""
字符串内建函数
1.capitalize()                                      将字符串的第一个字符转换为大写
2.center(width, fillchar)                           返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格,且必须为一个character
3.count(str,beg=0,end=len(string))                  返回str在string里面出现的次数，如果beg或者end指定则返回指定范文内str出现次数
4.bytes.decode(encoding="utf-8",error="strict")     使用 bytes 对象的 decode() 方法来解码给定的 bytes 对象，这个 bytes 对象可以由 str.encode() 来编码返回。
5.encode(encoding='UTF-8',errors='strict')          以 encoding 指定的编码格式编码字符串，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'
6.endswith(suffix, beg=0, end=len(string))          检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
7.expandtabs(tabsize=8)                             把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8,使用8个空格替换\t
8.find(str, beg=0, end=len(string))                 检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1
9.index(str, beg=0, end=len(string))                跟find()方法一样，只不过如果str不在字符串中会报一个异常.
"""
# capitalize()
str1 = "unicode字符串"
print(str.capitalize(str1))
# center(width, fillchar)
str2 = (str.capitalize(str1)).center(70, '-')
print(str2)
# count(str, sub)
sub = 'j'
str3 = "jowojqtklnkgakjdlfjalsdvnlkdkgkajdklf"
str.count(str3, sub)
print(str.count(str3, sub))
# decode() encode()
str_org = "这是一个已指定编码格式解码 bytees对象的函数，\t 默认编 码为utf-8"
str_utf8 = str_org.encode("utf-8", "strict")        # strict 编码错误引起的一个UnicodeError
str_gbk = str_org.encode("GBK", "ignore")           # 可以为ignore replace xmlcharrefreplace backslashreplace
print("UTF-8 编码", str_utf8)                       # 以及通过codecs.register_error() 注册的任何值
print("GBK 编码", str_utf8)
print("UTF-8 解码：", str_utf8.decode("utf-8"))
print("GBK 解码：", str_gbk.decode("GBK"))

# endswith(str,start,end)
suffix = "utf-8"
print(str_org.endswith(suffix, 0, 15))
print(str_org.endswith(suffix))
# expandtabs(8)
print(str_org.expandtabs(1))
# find(str, beg=0, en=len(string))
str_find = "这是一个find函数的列子！！！very good!!"
str_sub = "find"
print(str_find.find(str_sub, 3))
print(str_find.find(str_sub, 9, 20))
print(str_find.find(str_sub))
print(str_find.index(str_sub, 3))
# print(str_find.index(str_sub, 9, 20))               str_sub不在字符串中，会报异常
print(str_find.index(str_sub))
"""
字符串内建函数
10.	isalnum()                                         检测字符串是否由字母和数字组成，均为数字或者字母则返回True,否则返回False
11.isalpha()                                          检测字符串是否只由字母组成
12.isdigit()                                          检测字符串是否只由数字组成
13.islower()                                          检测字符串是否由小写字母组成,只要没有大写字母就返回true[数字和汉字都返回true]
14.isnumeric()                                        检测字符串是否只由数字组成
15.isspace()                                          字符串是否只由空白字符组成
16.istitle()                                          检测字符串中所有的单词拼写首字母是否为大写，且其他字母为小写
17.	isupper()                                         检测字符串中所有的字母是否都为大写
18.join(seq)                                          序列中的元素以指定的字符连接生成一个新的字符串
19.len(string)                                        返回对象（字符、列表、元组等）长度或项目个数
20.str.ljust(width[, fillchar])                       返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串
"""
# isalnum()
str_allnum = "1234jkjljakjkjkj234"
str_word = "卡机卡贷借款kjkjkjkjl23k4j3jk"
str_pha = "看经济可尽可能kjkljkjl"
str_noallnum = "卡机卡.贷借款kj.kjkjkjl23k4j3jk"        # 有汉字也会返回True
str_num = "1242359345023"
print(str_allnum.isalnum())
print(str_word.isalnum())
print(str_noallnum.isalnum())
# isalpha()
print(str_pha.isalpha())
print(str_allnum.isalpha())
# isdigit()
print(str_allnum.isdigit())
print(str_num.isdigit())
# islower()
str_big = "AADKJLklkjjlj2j3jkk"
print(str_allnum.islower())
print(str_word.islower())
print(str_big.islower())
# isnumeric()
print(str_big.isnumeric())
print(str_num.isnumeric())
# isspace()
str_space = "               "
print(str_big.isspace())
print(str_space.isspace())                  # tab也算空格
# istitle()
str_notitle = "Hello,world"
str_title = "Hello,World"
print(str_notitle.istitle())
print(str_title.istitle())
# isupper()
str_upper = "JKJKLJKJKJK"
print(str_upper.isupper())
print(str_title.isupper())
# join(seq)
s1 = "-"
s2 = ""
seq = ('r', '3', "dsj", '234', '344kk')
print(s1.join(seq))
print(s2.join(seq))
# len(s)
str_len = "k华kl就"
list_len = [1, 3, 4, 5, 5, 'kjkl', 5]
print(len(str_len))
print(len(list_len))
# str.ljust(width,[,fillchar])
str_ljust = "  this is a sample!!!!!"
print(str_ljust.ljust(50, '@'))
"""
21.lower()                                                转换字符串中所有大写字符为小写
22.lstrip()                                               截掉字符串左边的空格或指定字符
23.maketrans()                                            创建字符映射的转换表,第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。两个字符串的长度必须相同，为一一对应的关系。
24.max(str)                                               返回字符串 str 中最大的字母
25.min(str)                                               返回字符串 str 中最小的字母
26.str.replace(old, new[, max])                           把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。
27.rfind(str, beg=0,end=len(string))                      从右边开始查找
28.rindex( str, beg=0, end=len(string))                   类似于 index()，不过是从右边开始
29.rjust(width,[, fillchar])                              返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串。如果指定的长度小于字符串的长度则返回原字符串。
30.rstrip()                                               删除字符串字符串末尾的空格.                         
"""
# lower()
print(str_upper.lower())
#
# lstrip()
print(str_ljust.lstrip())
# str.maketrans(intab, outtab)
intab = 'aeiou'
outtab = '12345'
trantab = str.maketrans(intab, outtab)
str_trantab = "this is string example....wow!!!"         # 字符串中要替代的字符组成的字符串,相应的映射字符的字符串
print(str_trantab.translate(trantab))
# max(str)
print(max(str_trantab))
# min(str)
str_min = "thiskjkjgjakjdkalkwe..!!"                     # 空格是最小的
print(min(str_min))
# replace()
str_bereplce = "this is a english sentence,english"
print(str_bereplce.replace("english", "英文", 1))
# rfind()
str_rfind = "a b is is is is"
print(str_rfind.rfind('is', 0, 5))                        # 返回字符串最后一次出现的位置，如果没有匹配项则返回-1
print(str_rfind.rfind('is', 4, 16))
# rindex()
print(str_rfind.rindex('a'))
# rjust(width,[, fillchar])
str_rjust = "hahahahahhah"
print(str_rjust.rjust(50, '#'))
# rstrip()
str_rspace = 'jakjkjadjkljfalkd                     '
print(str_rspace.rstrip())
str_rspace = '*******jakjkjadjkljfalkd*********'
print(str_rspace.rstrip('*'))
"""
31.split(str="", num=string.count(str))                    返回分割后的字符串列表,num=string.count(str)) 以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num+1 个子字符串
32.splitlines([keepends])                                  按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
33.startswith(substr, beg=0,end=len(string))               检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False
34.strip([chars])                                          在字符串上执行 lstrip()和 rstrip(),该方法只能删除开头或是结尾的字符，不能删除中间部分的字符
35.swapcase()                                              方法用于对字符串的大小写字母进行转换
36.title()                                                 返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())
37.translate(table, deletechars="")                        根据 str 给出的表(包含 256 个字符)转换 string 的字符, 要过滤掉的字符放到 deletechars 参数中
38.upper()                                                 将字符串中的小写字母转为大写字母
39.zfill (width)                                           返回指定长度的字符串，原字符串右对齐，前面填充0
40.isdecimal()                                             检查字符串是否只包含十进制字符，如果是返回 true，否则返回 false。
"""
# split(str="", num=string.count(str))
str_split = "this is a sentence i want to translate this senten into a string list"
print(str_split.split(' '))
print(str_split.split(' ', 3))                             # 参数 num 有指定值，则仅分隔 num+1 个子字符串
# splitlines([keepends])
str_splitlines = "ab c \n ka\n\rsdfa\tdfad\r\n"
print(str_splitlines.splitlines())
print(str_splitlines.splitlines(True))
# startswith(substr, beg=0,end=len(string))
print(str_split.startswith('this', 3, 20))
print(str_split.startswith('this'))
# strip([chars])
print(str_rspace.strip('*'))
# swapcase()
print(str_split.swapcase())
str_split = str_split.capitalize()
print(str_split.swapcase())
# title()
str_split1 = "this is a sentence i want to translate this senten into a string list"
str_split1 = str_split1.title()
print(str_split1)
print(str_split1.swapcase())
# str.translate(table)
# bytes.translate(table[, delete])
# bytearray.translate(table[, delete])
intab = '12'
outtab = '男女'
table_a = str.maketrans(intab, outtab)
str_c = "张生1，王蕊2"
print(str_c.translate(table_a))
bytes_tabtrans = bytes.maketrans(b'abcdefghijklmnopqrstuvwxyz', b'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
print(b'hello,worrld.happy erverday'.translate(bytes_tabtrans, b'a'))
# str.upper()
print(str_split.upper())
# zfill()
print(str_split.zfill(90))
# isdecimal()
print(str_split.isdecimal())
print(str_num.isdecimal())
