#高阶函数--传入函数(map reduce filter sorted)返回函数,匿名函数 装饰器 偏函数
from functools import reduce
import  functools
print('--------------传入函数----------------------------------------------')
#变量可以指向函数 如 abs()这个求绝对值
f=abs
print(f(-3.5)) #这里我们就把abs()函数给了f f也就相当于abs()
#函数名也是变量  只是一个指针变量而已 他指向一个可以计算绝对值的函数而已
#abs=10 #ok 现在这个指针让我们改变指向了  那也就无法拿来 做计算绝对值的运算了 print(abs(-3.5)) 很显然会报错 当然实际开发可千万别这么写
# 由于abs实际上定义在 import  builtins 中 所以我们要让修改abs指向在其他模块也生效 import  builtins;  builtins.abs=10 千万别做啊
print('--------------map-------')
#(1)map/reduce

#python 内建了map()和reduce()函数
#map(function(),Iterable) 接收两个参数 一个是函数 一个是Iterable(可迭代对象--list tuple str dict set generator)
#map将传入的函数依次作用到序列每个元素,并把结果作为新的Iterator返回
#简单点说就是把Iterable所有元素都用前面函数处理一下
def f(x):
    return x*x

r=map(f,[1,2,3,4,5,6,7,8]) #此时r为一个Iterator
print(list(r)) #[1, 4, 9, 16, 25, 36, 49, 64] 我们可以看到f(x)把x*x的操作都赋予了list每一个元素
print(list(map(str,[11,22,33,44]))) #这个我们一下子就可以理解 把[11,22,33,44] 全部变为字符串
print(list(map(abs,[11,-0.25,-2.5,44])))
print('--------------reduce-------')
#reduce(function(),Iterable)  这个函数必须接受两个参数 简单的理解就是 reduce(f,[x1,x2,x3,x4])=f(f(f(x1,x2),x3),x4) 先取前两个元素进行函数运算 把结果和第三个运算再把结果和第四个运算
#这个需要导入 from functools import reduce
def add(x,y):
    return  x+y
print(reduce(add,[1,2,5,6,9])) #当然求和我们可以用 sum 但是要是把[1,2,5,6,9]变成 12569
def fn(x,y):
    return x*10+y
print(reduce(fn,[1,2,5,6,9]))

#这里我们利用map和reduce的特性写一个str转int
#'125486'-->125486  第一 把'125486'每一个字符拆分出来并变为int 第二步用reduce递增特性进行拼接
DIGITS={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
def chartonum(s):
    return DIGITS[s]  #这个就把对应的int类型拆分的值返回
print('\'125486\'-->',reduce(fn,map(chartonum,'125486')))

#总结一下   map----每个都进行函数处理   reduce----两两运算,结果传递 应用:数字拼接 1 2 3 5->1235  等等

print('----------filter--------')
#(2)filter
#和map类似 也是传入函数和序列 把序列的每一个元素作用于函数 根据返回值是True 还是 False 保留还是丢弃 并把结果作为新的Iterator返回
#比如我们删除偶数
def is_odd(n):
    return n%2==1
print(list(filter(is_odd,[1,2,3,4,5,6,7,8,9])))
#把一个序列中空字符删除
def not_empty(s):
    return s and s.strip() #strip()用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
print(list(filter(not_empty,['A','',None,'','C',' ']))) #['A', 'C'] 从结果我们看到 '',' ',None都被移除了
#计算素数 这个很有用
#这里我们使用---埃氏筛法 首先从2开始 把2的倍数全部删除 取新序列3的倍数全部删除 <!---埃氏筛法筛完的序列第一个元素一定是素数--->
def _odd_iter(): #这里我们创建一个生成器 一个无限序列 一个从3开始的奇数序列 因为偶数肯定不是素数
    n=1
    while True:
        n=n+2
        yield n
#下面我们定义筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0  #  lambda x, y: x*y；函数输入是x和y，输出是它们的积x*y
#最后定义一个生成器 不断返回下一个素数
def primes():
    yield 2
    it=_odd_iter() #初始化序列 3 5 7 9 ........
    while True:
        n=next(it) #取出一个 3 5 7 9 ........
        yield  n #每次输出一个n 注意第一个输出的就是3
        it=filter(_not_divisible(n),it) #构造新序列 把it中能被n整除的元素过滤掉(删除掉) 埃氏筛法
        # 在第一次执行的时候 n=3很明显是false 所以it中3被删除 但是上一步yield  n保留了3 所以输出还是有3 因为我们根据yield  n输出,然后it不断通过filter进行更新
        #埃氏筛法筛完的序列第一个元素一定是素数 所以我们才可以直接取新的序列第一个元素

#打印100以内素数
for n in primes():
    if n<100:
        print(n)
    else:
        break

print('----------sorted--------')
#sorted 排序
print(sorted([15,545,84,5,42,64]))
#我们甚至可以加入函数辅助进行排序 如加入abs函数
print(sorted([15,-24,-2,5,-40,64], key=abs)) #[-2, 5, 15, -24, -40, 64] 我们可以看一下结果 可以看到-24 排在了15 前面
print(sorted(['Cf','Ag','Gr','Fr','Ga'])) #ASCII进行比较
print('--------------返回函数----------------------------------------------')

#所谓返回函数 指的是我们把函数作为返回值返回 这样我们可以延迟计算 在用到求和的地方在计算
#下面我们来返回一个求和的函数
def lazy_sum(*args):
    def sum():  #这里内部的sum 可以调用外部lazy_sum的参数和局部变量
        ax=0
        for n in args:
            ax=ax+n
        return ax
    return sum #当lazy_sum返回sum函数时,<!----相关参数和变量都保存在返回函数中,但是没有运行哦  这种我们称之为闭包----->
f=lazy_sum(2,5,6,47,8) #我们返回一个求和函数给f
f1=lazy_sum(2,5,6,47,8) #这里每次调用都返回一个新的sum 即使传入相同的参数 两者返回结果互不影响
print(f(),f1())
#闭包---外部函数正常执行 即使for循环也是正常执行 内部返回函数不执行 但是参数会不停地被外部函数覆盖,填充
print('--------------匿名函数----------------------------------------------')

print(list(map(lambda  x: x*x,[1,2,5,3,6,8,5])))

#这里需要着重说一下匿名函数lambda用法---他是用来定义一个函数的 和def差不多 但是他更加短小精悍  格式---lambda x:x*x
#filter函数。此时lambda函数用于指定过滤列表元素的条件。例如filter(lambda x: x % 3 == 0, [1, 2, 3])指定将列表[1,2,3]中能够被3整除的元素过滤出来，其结果是[3]。

#sorted函数。此时lambda函数用于指定对列表中所有元素进行排序的准则。例如sorted([1, 2, 3, 4, 5, 6, 7, 8, 9], key=lambda x: abs(5-x))将列表[1, 2, 3, 4, 5, 6, 7, 8, 9]按照元素与5距离从小到大进行排序，其结果是[5, 4, 6, 3, 7, 2, 8, 1, 9]。

#map函数。此时lambda函数用于指定对列表中每一个元素的共同操作。例如map(lambda x: x+1, [1, 2,3])将列表[1, 2, 3]中的元素分别加1，其结果[2, 3, 4]。

#reduce函数。此时lambda函数用于指定列表中两两相邻元素的结合条件。例如reduce(lambda a, b: '{}, {}'.format(a, b), [1, 2, 3, 4, 5, 6, 7, 8, 9])将列表 [1, 2, 3, 4, 5, 6, 7, 8, 9]中的元素从左往右两两以逗号分隔的字符的形式依次结合起来，其结果是'1, 2, 3, 4, 5, 6, 7, 8, 9'。

print('--------------装饰器----------------------------------------------')
#在代码运行时动态的增加功能的方式我们称之为装饰器(decorator)
#本质上 decorator是一个返回函数的高阶函数    比如我们要定义一个可以在函数调用前后打印日志的装饰器
def log(func):
    def wrapper(*args,**kw):  #*args,**kw 因此就可以接受任意参数调用 当然去掉也可以不影响结果 毕竟只是打印
        print('this is  log')       #函数对象有一个 _name_可以拿到函数名称
        return func(*args,**kw)  #我们可以看到返回的还是now函数 不同的是 在now函数返回之前 加上了 print 输出日志
    return  wrapper

@log #我们需要在这个函数执行前打印日志  借助@log 相当于now=log(now)
def now():
    print('2019-11-3')
now()
#如果我们本decorator 需要参数 那么我们写出的程序可能更加负载
def log2(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print('%s this is  log' % (text))
            return func(*args,**kw)
        return wrapper
    return decorator
@log2('excute')  #相当于now=log2('excute')(now)
def now2():
    print('2019-08-15')
now2()  #首先@log2('excute') 返回 decorator 在调用decorator函数 参数是now  返回wrapper 函数此时wrapper函数没有执行,只是参数填充完毕 now2执行的时候才开始执行

print('--------------偏函数----------------------------------------------')
#偏函数--从前我们可以给参数添加默认值的方式来给降低函数的调用难度.而偏函数也可以也可以做到这一点
#以函数为基础 ,为函数设置默认值  返回一个新的函数
print(int('12345',base=16)) #int() 提供额外的base 参数 默认值是10   传入base参数可以做N进制转换
print(int('12345',8)) #当然可以省掉 base
#假设我们需要大量转换二进制字符串
def int2(x,base=16):  #要注意的是python3.8好像无法用int进行2进制转化按
    return int(x,base)

print(int2('545'))

#下面我们来创建一个偏函数 要导包 import  functools

int3=functools.partial(int,base=8) #以函数int 为基础 ,为int函数设置默认值 返回一个新的函数

print(int3('100020')) #32784

#类似的还有 max
max2=functools.partial(max,10)
print(max2(5,6,7))  #结果是 10   虽然传入了 5 6 7 但是 10 也是默认值的形式保留了下来