#列表生成项 生成器 迭代器
#我们可以很方便用 l = list(range(1,11))  # 生成[1--10]数 但是要是生成[1*1,2*2,3*3,.....10*10] 我们就需要用到循环
from collections import Iterable
from collections import Iterator
l=[]
for x in range(1,11):
    l.append(x*x)
print(l)
#下面我们使用列表生成项
l1=[x*x for x in range(1,11)] #意思很好懂 我要生成 x*x这个 x从 x in range(1,11) 取得
print(l1)
#我们还可以使用两个未知数
l2=[m*n for m in 'ABC' for n in [1,2,3]] # A-1 A-2 A-3 B-1 B-2 B-3 C-1 C-2 C-3 重点注意'*'这个代表的意思
print(l2)
l3=[m+n for m in 'ABC' for n in 'XGF'] #需要注意 这种组合方式 '+' 数字是加上  str 是组合 如果这里我们换成'*' 就会报错
print(l3)
#例子 列出当前目录下所有文件和目录名字
import  os
l4=[d for d in os.listdir('.')]
print(l4)
#下面我们做一个很有意思的事情 把tuple 变为 list 同时我们把字母都变成大写的
tu={'a':'A','b':'B','c':'C'}
l5=[(k+v).upper() for k,v in tu.items()]
print(l5)  #['AA', 'BB', 'CC'] 被我们组合到一起去了 并且 字母都是大写的
#生成器 列表生成项会占用很多内存 但是如果我们只要访问最后几个 那么前面的不就全部浪费了吗
#所以我们引入生成器-一边循环 一边计算  创建的方法超级简单 把[]变为()就ok了 这只是第一种创建generator 的方式
g=(x*x for x in range(10))
print(next(g),next(g)) #0 1 从结果我们可以看出  每次调用一个next() 都输出一位
for g1 in g:   #我们一般使用这个方法来输出
    print(g1)
#做个简单例子 斐波那契数列 可以从第一个元素推算出后续元素 这个原理就和generator 是一样的 我们在print(b) 变为 yield b 是第二种创建generator 的方式
#当一个函数含有yield的关键字时 那么它就会变为一个 generator
print('-----------------------------')
def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield  b #print(b) 就是传统的算法
        a,b=b,a+b
        n=n+1
    return 'done'
#这里 注意一下a,b=b,a+b  相当于
#t=(b,a+b)
#a=t[0]
#v=t[1]
f=fib(12) #函数体有yield 关键字 所以变为了 generator
print(next(f))
for f1 in f:   #我们一般使用这个方法来输出
    print(f1)

#下面我们来探讨一下 函数的顺序执行流程--遇到return 或者 最后一行函数语句返回 和 generator--每次调用next()执行 遇到yield 语句返回,再次执行上一次返回的yield语句继续执行
print('-----------------------------')
def odd(): #我们先来生成一个generator
    print('step1')
    yield 1
    print('step2')
    yield 2
    print('step3')
    yield 5

o=odd()
print(next(o))
print(next(o))
print(next(o)) #从中我们可以清晰的看见 每次执行都是从上一次yield的地方向下执行 每次执行到yield 返回 当然实际上我们不用next()
print('-----------------------------')
for o1 in odd():
    print(o1)

#迭代器
print('--------------可迭代对象 ---------------')
#我们知道可以直接使用for的可迭代对象有 一类集合数据类型---list,tuple,dict,set,str 第二类generator 包括生成器和带yield的函数
#我们可以使用 isinstance(,Iterable) 来判断是否是  --------------可迭代对象(和迭代器对象是两回事)  from collections import Iterable

print(isinstance([],Iterable))
print(isinstance((),Iterable))
print(isinstance({},Iterable))
print(isinstance('abc',Iterable))
print(isinstance((x for x in range(10)),Iterable)) #generator 可以
print(isinstance(100,Iterable)) #整数不行

print('--------------迭代器对象 ---------------')
#迭代器对象-----可以作用于for 并且 可以使用next函数返回下一个值 我们才称之为 迭代器对象
#我们可以使用 isinstance(,Iterator) 来判断是否是  --------------迭代器对象 from collections import Iterator
print(isinstance([],Iterator)) #list 不行
print(isinstance((),Iterator))#tuple 不行
print(isinstance({},Iterator))#dict 不行
print(isinstance('abc',Iterator))#str 不行
print(isinstance((x for x in range(10)),Iterator)) #generator 可以
#当然python 也提供了 把 list dict tuple str 变成迭代器的方法 iter()
print('----------------------------')
print(isinstance(iter([]),Iterator))
