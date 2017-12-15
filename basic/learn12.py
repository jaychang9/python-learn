# -*- coding: utf-8 -*-

def calc(*nums):
    sum = 0
    for num in nums:
        sum += num * num
    return sum

# 可传list, *l可以将list转为可变参数
l = [1,2,3]
print(calc(*l))

t = [1,2,3]
# 可传tuple,*t可以将tuple转为可变参数
print(calc(*t))

# 可传任意个参数个数
print(calc(1,2,3))
