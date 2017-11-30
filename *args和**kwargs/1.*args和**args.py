#coding:utf8
'''
首先明确一点，*args和**kwargs中，重要的是星号，也就是说，你写成*var和**vars也是可以的
'''

#args的使用
'''
*arg和**kwargs经常在函数定义中使用，*arg和*kwargs作用是像函数中传递很多参数。
很多的含义是你不知道要传递多少参数。
*arg的作用是传递很多"非关键词"参数
Eg：
'''

def var_args(f_arg, *argv):
    print('first normal arg:', f_arg)
    for arg in argv:
        print ('another arg through *argv:', arg)

var_args('yasoob', 'python', 'eggs', 'test')

#可以说很明确了
#又思考了一步，'for arg in argv:'说明argv只是变量，*是符号，二者是分开的；
#同时也说明argv是一个类似列表的可迭代的。

#**kwargs的使用
'''
**kwargs用来传递"关键词"变量，是对应的
'''

def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))

greet_me(name='yasoob')

#**去指代kwargs是一个字典，有键有值


#一起使用
def args_kwargs(arg1=11, arg2=12, arg3=13):
    print('arg1:', arg1)
    print('arg2:', arg2)
    print('arg3:', arg3)

args = {'arg1':1, 'arg2':2, 'arg3':3}
args_kwargs(**args)

#这说明了什么，用*来解列表，用**来解字典
#据说在装饰器上面用得多