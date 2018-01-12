# -*- coding: utf-8 -*-

import functools

def normalize(name):
    return name.title()


r = list(map(normalize,['Addd','bbbbasdf','cDDD']))

print(r)


# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


def prod(L = []):
    return functools.reduce(lambda x,y:x*y,L)

print(prod([1,2,3,4,5]))

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')