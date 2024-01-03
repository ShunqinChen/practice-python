# 函数定义及参数

from audioop import mul


def multi(a,b=1):
    return a*b

# 有默认值时可以只传入一个参数
result = multi(3)
print(result)

# 也可以传入多个参数覆盖有默认值的参数
result = multi(3,2)
print(result)