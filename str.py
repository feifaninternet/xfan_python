# string

var1 = 'hello World'
var2 = 'Python'

# 访问值
print(var1[0])
print(var2[1:5])

# 字符串常用方法
# 1.capitalize() 字符串首字母大写
print(var1.capitalize())

# 2.count() 统计字符串出现的次数
print(var1.count('o'))

# 3.center() 打印输出字符串，让字符串处于中间
print(var1.center(20, '*'))

# 4.endswith() 判断是否以指定的字符串结尾
print(var1.endswith('d'))

# 5.find() 查找指定字符串在原字符串中第一次出现的位置，返回所在索引
print(var1.find("h"))
word = var1[var1.find('h'):var1.__len__()]
print(word)

# 6.format() 字符串替换,字符串中要有{}标识
var3 = 'Hello World is {}'
var4 = 'Hello World is {1} {0}'
formatStr = var3.format('normal')
formatStr2 = var4.format('normal', 'so')
print(formatStr)
print(formatStr2)

# 7.isalnum() 判断字符串中是否全部为英文或者数字
allNumStr = 'helloWord'
print(var1.isalnum())
print(allNumStr.isalnum())

# 8.isalpha() 判断是否全为英文
print(var1.isalpha())

# 9.isdigit()判断字符串中是否全部为整数
test = '123'
print(var1.isdigit())
print(test.isdigit())

# 10.islower() 判断是否全部为小写 isupper() 判断是否全部为大写
print(var1.islower())
print(var1.isupper())

# 11.lower() 将字符串变为小写 upper() 将字符串变为大写
print(var1.lower())
print(var1.upper())

# 12.join() 连接字符串，将列表中的元素以指定的字符连接成一个新的字符串
name = ['xfan', 'mark', 'selina']
print('_'.join(name))

# 13.replace(ole,new,count) 字符串替换,count为替换个数
print(var1.replace('l', 'x', 2))

# 14.split() 切割
vector = 'anb,and,hollwers'
print(vector.split(','))

# Python中的字符串只能覆盖不能修改
# error
var5 = 'xfan'
var5[0] = 'h'
print(var5)

# right
var5 = 'xfan'
var5 = 'hfan'
print(var5)

