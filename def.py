# Python 中的函数
import str

def test(a):
    print(a)
    return


test('abc')

'''
    不可变对象: strings,tuples,numbers
    可变对象: list,dict
'''


# 传不可变对象
def test2(a):
    a = 10


b = 2
test2(b)
# b的值不会被改变
print(b)


# 传可变对象
def changeList(cusList):
    cusList[3] = 4


list1 = [1, 2, 3, 'b']
changeList(list1)
# list1的值被改变
print(list1)

# ===================== 函数的参数 =======================
'''
    1.必备参数
    参数必须以正确的顺序传入函数，调用时的数量必须和声明时的一样
'''


def mustParamter(str):
    print(str)
    return


mustParamter('a')
# 报错
# mustParamter()

'''
    2.关键字参数
    允许函数调用时的参数顺序与声明时不一致，因为Python解析器能够通过参数名匹配参数值
'''


def customerPrint(str):
    print(str)
    return


customerPrint('hahha')

'''
    3.缺省参数
    缺省参数的值如果没有传入则视为使用默认值
'''
def printInfo(name, age = 24):
    print("name:", name);
    print("age:", age);
    return


printInfo('xfan', 50)
printInfo('xfan')

'''
    4.不定长参数
    不定长参数比函数当初声明时的参数更多
'''
def noSureParam(arg1,*args):
    print(arg1)
    for var in args:
        print(var)
    return


noSureParam(12, 'xfan', 24, 48)

'''
    匿名函数:
    1.lambda只是一个表达式，函数体比def简单
    2.lambda的主体是一个表达式，而不是一个代码块，仅仅能在lambda只能封装有限的逻辑进去
    3.lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数
'''
sum = lambda arg1, arg2: arg1 + arg2;
print(sum(1, 2))

'''
    变量的作用域:
    变量分为全局变量和局部变量
    通过下面的函数示例我们来了解一下这两个变量的作用范围
'''
total = 'xfan'
def testTotal():
    total = 24
    print("局部变量total:", total)

# 输出局部变量 24
testTotal()
# 输出全局变量‘xfan’
print("全局变量total:", total)
