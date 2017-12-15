# -*- coding: utf-8 -*-

# 可变对象与不可变对象

a1 = 'abc'

a2 = ['a','b','c']

a11 = a1.replace('b','bb')

a2.pop(2)

# a1是没变的
print('a1 = %s,a11 = %s' % (a1,a11))

# a2已经变了
print('a2 = %s' % a2)


