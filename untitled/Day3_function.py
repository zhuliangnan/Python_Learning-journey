#函数的使用与定义
#abs(x) 绝对值
print(abs(-97.4))
#max(a,b,c,d...) 返回最大值
print(max(1.9,1.7,9.0,6))
l=[1,6,9,4,79]
print(max(l))#显然它也可以接受 list类型
#类型转换函数 int() str() bool()
print(int('657'))
#print(int('a')) 这个是不行的
print(str(234.8))
print(bool(-1),bool(4),bool('a'),bool(''),bool(0))#空字符串和0都是false
print('this is following is def function()\n')

#函数定义 def
def myfirst_fun(x):
	if x>=18:
		return 'adult'
	else:
		return 'child'
print(myfirst_fun(23))
#如果我们把myfirst_fun 保存在 abstest.py中 我们可以使用 from abstest import myfirst_fun 来导入，具体表现为
#from abstest import myfirst_fun
#myfirst_fun(23)
#如果要定义一个什么都不干空函数 用pass 其作用在于现在不知道想运行什么写什么代码 可以作为占位符使用 以后想起来了在写
def nop(x):
	if x<=0:
		pass
print(nop(-6))
#可以返回多个值 实际上是返回一个tuple
#这里值得关注的是angle=0为默认值 我们可以不给这个值 默认参数一定要指向不可变的值
import  math
def move(x,y,step,angle=0):
	nx=x+step*math.cos(angle)
	ny=y-step*math.sin(angle)
	return nx,ny
x,y=move(100,100,60,math.pi/6)
print(x,y)
print(move(100,100,60,math.pi/6))#这里我们可以发现其实返回的还是一个值 tuple
print(move(100,100,math.pi/6))#我们这里不给angle的值它默认就是0