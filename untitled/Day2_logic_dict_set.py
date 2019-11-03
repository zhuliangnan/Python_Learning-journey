# 顺序逻辑判断选择 dict set
# 对于if 相关if语句直接应当保持一致的缩进 且if的缩进一定在执行体前面
age = 20
if age <= 17:
    print('年龄小于17')
    print('adult')
else:
    print('年龄大于17')
    print('adult')

age2 = 30
if age2 <= 18:
    print('age less than 18')
elif age2 >= 20:
    print('age more than 20')

if 2:
    print('this is no none')

if True:
    print('this true is no none')
# input方法返回的是str 字符串需要用int（）函数进行转换
# birth=input('please set your birth year')
# birthreal=int(birth)
birthreal = 1996
if birthreal <= 2000:
    print('you are no puple')
else:
    print('get out and doing your homwork')

print('this following is for\n')

classroom = ['aaa', 'bbb', 'ccc', 'ddd''eee', 'fff']
# 有点类似于 java的强制for
for name in classroom:
    print(name)

# 要注意的是如果下面我的print()与sum=sum+number一个缩进，他会把这个print看成for循环的一部分哦
sum = 0
for number in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + number
print(sum)
# 下面简绍一个函数range()用于生成整数序列，从0开始 list()用于把数据直接装入list
l = list(range(9))
print(l)
print(list(range(100)))

print('this is following is while\n')

sums = 0
n = 99
while n > 0:
    if n % 2 == 0:
        print('this is oushu', n)
        n = n - 1
        continue
    sums = sums + n
    n = n - 3
    if sums > 200:
        break
print('sums is', sums, 'now n is', n)

print('this is following is dict set\n')
# dict=map 值得注意的是写的时候用{}  拿的时候用[] 且dict采用索引查找 查找速度快 请注意存放顺序和key放入顺序没有关系
score = {'zhu': 80, 'chen': 78, 'li': 90}
print(score['zhu'])
score['chen'] = 67
print(score['chen'])
# 可以使用 in或者get()来查询key存在与否
print('zhu' in score)
print(score.get('xia'))  # 存在会返回相对应的值 不存在返回none
# 值得注意的是 为了保证hash值的正确性 key所使用的对象必须的不可变 如str 整数 但是list是可变的不可以作为key

print('thiz is following is set\n')
# set是一组key的集合 不存储 value ，且不存储重复的key 重复元素会被自动过滤掉 传入的参数是list
s = set([1, 1, 2, 2, 3, 4, 5, 5, 6])  # 这里会把重复元素去掉 并且显示顺序也不表示set是有序的
print(s)
s.add(9)
print(s)
s.remove(5)  # 这里删除的key 不是下标 set里面没有下标一说
print(s)
s1 = ([1, 2, 3, 4, 7])
s2 = ([1, 3, 5, 8, 10])
# s1|s2并集 s1&s2 交集  s1-s2 差集 这个我没有做出来可能版本不一样
a = ([9, 10, 2, 3, 4, 6, 8])
a.sort()
print(a)

