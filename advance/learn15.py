# -*- coding: utf-8 -*-
def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))


L = list(filter(lambda n:n % 2 == 1,range(1,20)))
print(L)

f = is_odd

print('function name = %s' % f.__name__)

print('function name = %s' % (lambda x:x*x).__name__)