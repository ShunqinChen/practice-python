#!/usr/bin/env python3
print("hello world")

print("hello","world","with","serveral","words")

print("Expression: 100+200=",100 + 200)

name = input("Please input your name:") # input 输入为字符串，如果要用数字需要转型
print("hello,",name)


# 多行字符串
print('''
    Hello gentlely word!
        Merry Christmas!
''')

# r'' 声明单引号内容部转义
print('tanbii \n world \\')
print(r'tanbii \n world \\')

# 变量替换
text= 'world'
print(f'hello {text}')

# 转义
print( '\u4e2d\u6587')

## if
if 1:
    print(2)
    print(3)
print(4)

## for
item = 1
for item in [1,2,3]:
    print(10)


    print(15)
    item = item+1