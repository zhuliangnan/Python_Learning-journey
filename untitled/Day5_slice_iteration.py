
# 切片(Slice)
from collections import Iterable
l = ['joy', 'jack', 'uzi', 'faker']
print(l[0:3])  # print(l[:3]) 当然第一个下标是0也是可以省略的
# 又比如
l = list(range(100))  # 生成0--99数
print(l[:])  # 它代表从开始一直取到结束 一个闭环
print(l[90:100])  # 他代表的意思是 从下标l[90] 开始 一直取10个数
print(l[-10:])  # 也是取后10个
print(l[10:20])  # 从下标10开始 一直取10个数 l[10]-l[19]
print(l[:10:2])  # 从下标0开始 每两个取一个
print(l[::5])  # 每五个取一个
# 同样的 tuple 也是一种不可变得list 所以也可以进行切片操作
print('this is following is tuple\n')
tu = tuple(range(100))
print(tu[:])
print(tu[90:100])  # 我们发现结果是一样的
print('this is following is 迭代\n')
# 迭代 python 的for循环 不仅仅可以对list tuple 进行 甚至可以被用来使用在dict 等其他没有下标的可迭代对象
# 请记住 dict存储并不是顺序的 所以 迭代出来的 顺序可能不一样
di = {'a': 1, 'b': 'bei', 'c': 1.8}
# 迭代key
for key in di:
    print(key)
# 迭代values
for values in di.values():
    print(values)
# 迭代values and key
for items in di.items():
    print(items)
# 那么我们怎么判断可以迭代的对象呢 通过 collections的iterable类型判断

# from collections import Iterable 导包 这一步在本文档最上面
print(isinstance('str', Iterable))
print(isinstance([1,2,3], Iterable))
print(isinstance({'a':1,'b':2}, Iterable))
print(isinstance(1, Iterable)) #我们可以看出 整数不可以迭代\

#补充如果我们 要输出list 下标 怎么办呐 使用 enumerate 它可以把 list 变为 索引-元素 这种数据结构
l=['aa','cc',1.78,'dd']
for i,value in enumerate(l):
    print(i,value)
for i,value in [(1,2),(4,5),(7,5)]:
    print(i,value)
