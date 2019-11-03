#格式化
print("hello")
name=input('请输入姓名')
print('你输入的姓名是: ',name)
print('\\i\'am your \n')
print('father')
print('''line1
lin
e
2line
3''')
print('3/2=',3/2) #一定表示为浮点型
print('6/2=',6/2) #一定表示为浮点型
print('3//2=',3//2) #整除
print(ord('A'),ord('中'),chr(25991),chr(66))
x=b'A'
print(x)
#y=b'中国' print(y)  这个方式是错的
#Python中的字符串类型是str 在内存中表示为Unicode编码 一个字符表示若干字节 在网络上传输需要把str变为 以字节为单位的bytes
print('A'.encode('ascii')) #把纯字母的str 用ASCII编码为bytes 要注意的是为了避免乱码我们应当始终坚守使用utf-8进行编码
print('中文'.encode('utf-8')) #把中文的str 用utf-8编码为bytes
print(b'A'.decode('ascii')) #bytes ->ASCII编码
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')) #bytes ->utf-8编码
print(len('ABC'),len('中国')) #len()函数计算字符数 如果换成bytes计算字节数
print(len(b'ABC'),len(b'\xe4\xb8\xad\xe6\x96\x87'),len('中文'.encode('utf-8')))  #由此可见一个中文字符 占3个字节
