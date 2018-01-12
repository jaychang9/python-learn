# -*- coding: utf-8 -*-
import os

print(['D:/PythonWorkspace/PythonLearn'+d for d in os.listdir('../') ])

print([m+n for m in 'ABC' for n in 'XYZ'])

d = {'x': 'A', 'y': 'B', 'z': 'C' }

print(['k='+k+',v='+v for k,v in d.items()])


L = ['Hello', 'World', 'IBM', 'Apple']

print([str.lower() for str in L])


L1 = ['Hello', 'World', 18, 'Apple', None]

print([x.lower() for x in L1 if isinstance(x,str)])

L2 = [x.lower() for x in L1 if isinstance(x,str)]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')