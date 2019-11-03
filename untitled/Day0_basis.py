#基础 list tuple
print('100+200+300')
#格式化
print('hi %s hfyd %d  ' % ('htddt',166))
print('{0} cjrj {1}rffr'.format('chenan',233))
#list
classmates=['zhu','cheb','li']
classmates.append('pan')
print(classmates,len(classmates),classmates[0],classmates[1],classmates[2],'lastelem',classmates[-1])
classmates.insert(1,'jackchen')
print(classmates)
classmates.pop(1)
print(classmates)
classmates[2]='jackma'
print(classmates)

print('\n')
l=['apple',354,True,['zhu','chen',True],'last']
print(l)
print(l[3][2])

print('\n')
#tuple 不可变对象 list＋不可变
classbytuple=('aa','bb','cc')
print(classbytuple)
print(classbytuple[2])
tuple=('aaa','bbb',[726,'hsha'])
tuple[2][0]=122
tuple[2][1]='hsgs'
print(tuple)