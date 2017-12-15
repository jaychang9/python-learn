# -*- coding: utf-8 -*-

# 第一部分 dict学习
d = {'jay':87,'lily':90,'jack':60}

print(d['jay'])

d['james'] = 88

print(len(d))

for k in d:
    print('key = %s,value = %s' % (k,d[k]))



# 如果通过d['xx']查找一个不存在的值时会报错，可以使用d.get('xx'),当不存在时会返回None

print(d.get('xx'))

# 如果通过d['xx']查找一个不存在的值时会报错，可以使用d.get('xx',-1),当不存在时会返回自定义值-1

print(d.get('xx',-1))


# 删除一个键值对用pop方法

print(d)

d.pop('jay')

print(d)


# 第二部分 set学习

# set里存放的是不重复的数据
s = set([1,2,3,3,4])

print(s)

s.add(22.22)

s.add('a')

s.add('A')

s.add(4)

s.add(0.1)
s.add(11.22)

s.add(5)

print(s)


# 集合交集、并集

s1 = set([1,2,3,4,88,66])

s2 = set([0,2,3,4,5])

print(s1 & s2)

print(s1 | s2)