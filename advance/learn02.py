# -*- coding: utf-8 -*-
from collections import Iterable

d = {'k1':'v1','k2':'v2','k3':'v3','k4':'v4','ka':'va','kb':'vb','kc':'vc'}

for k,v in d.items():
    print('k:',k,'v:',v)


for k in d:
    print('k:',k,'v:',d.get(k))


for v in d.values():
    print('v:',v)


print(isinstance('abc',Iterable))

print(isinstance((1,2,3),Iterable))

print(isinstance([1,2,3],Iterable))


print(isinstance(d,Iterable))

print(isinstance(1,Iterable))


def findMinAndMax(L):
    if [] == L:
        return (None,None)
    if len(L) == 1:
        return (L[0],L[0])
    min = L[0]
    max = L[0]
    for i in L:
        if i < min:
            min = i
        if i > max:
            max = i
    return (min,max)


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
