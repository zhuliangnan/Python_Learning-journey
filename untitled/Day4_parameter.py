# 参数 可变参数 关键字参数
# 所谓可变参数指的是 <!--参数的个数可变--> 在参数前面加上*就可以了
def calc(*number):
    sum = 0
    for n in number:
        sum = sum + n * n
    return sum


print(calc(1, 2))  # 这里我们传入两个参数
print(calc())  # 不给参数也可以
# 那么问题来了 如果我们要传入的就是list 或者tuple 怎么办 总不能作为一个参数传入
# 当然 calc(list[0],list[1],lis[2])也是可以的 但是很蠢 我们采用以下的方法
list = [1, 2, 3, 5, 6]
calc(*list)  # *list 表示吧这个list所有元素作为 可变参数传进去 这种写法才是常见的


# 关键字参数  在参数前面加上**就可以了 他允许传入<!--任意个包含参数名的参数-->
def person(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:', name, 'age:', age, 'other', kw)  # 没有给return 会自己返回none


person('zhu', 23)
person('zhu', 23, city='beijing', zip=15454)  # 传入带有参数名字的参数
person('zhu', 23, city='beijing', job='IT')

extra = {'city': 'beijing', 'job': 'IT'}  # 我们甚至可以使用 dict类型 {map}
person('zhu', 23, **extra)


# 命名关键字参数 当然 python 也提供了一种把参数写死的方法 即不允许传输那么多参数  只需要在参数前面加个*就可以限定后面参数个数
# 需要注意的是 命名关键字参数 <!---必须传入参数名字 city='beijing'--->
def people(name, age, *, city, job):
    print('name:', name, age,'age','city:', city, 'job', job)


people('nan', 23, city='beijing', job='IT')
#如果前面已经有一个可变参数 *args 后面的的命名关键字参数就不需要一个分隔符*了
def people2(name,age,*args,city='beijing',job):
    print('name:', name, age,'age', args,'args', city, 'city', job,'job')


people2('zhu',23,(2,5,'nan'),job='IT') #这里由于 city已经有一个默认值了正常来说我们是可以赋值的 但是这里作为命名关键字由于它的限制作用 只有接收一个 默认值已经占据了 所以不可以再接受了 所以这里我们不可以再给它值  否则会报错

#参数组合  我们可以吧必选参数 默认参数-可变参数(*)-命名关键字参数(前面放一个*)-关键字参数(**) 进行组合 但是注意 顺序就是这个顺序 不可以反了
def com(a,b,c=0,*arg,city,job,**kw):
    print('a',a,'b',b,'c',c,'arg',arg,'city',city,'job',job,'kw',kw)
l={'class':'2162','professonal':'计算机'} #dict(map)
tup=('zhuzhu',23) #tuple
com(1,'zhuzhu','13',['nan','ge','nb'],city='beijing',job='IT',**l)
#a 1 b zhuzhu c 13 arg (['nan', 'ge', 'nb'],) city beijing job IT kw {'class': '2162', 'professonal': '计算机'}
#这里重点看一下 arg (['nan', 'ge', 'nb'],) 这里我们刚刚存进来的list 但是还是再转成了 tuple  总结在最后
com(tup,('nan','ge','nb'),'c1',city='beijing',job='IT',**l)
#注意
#*args 是可变参数 接收的是 tuple 即使你给他list 也会变成 tuple  既可以直接从传入 func((1,2,3)) 也可以 tup=(1,2,3) func(*tup)
#**kw 是关键字参数  接收的是一个dict(map) 既可以直接传入 func(a=1,b=1) 也是可以 dict={'a':1,'b':2}  func(**dict)
#命名关键字不要忘记写 *作为分隔符