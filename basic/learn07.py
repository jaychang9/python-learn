# -*- coding: utf-8 -*-

def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-2))

print(my_abs(-2.2))

print(my_abs(0))

print(my_abs(100))

# python会进行参数个数检查 TypeError: my_abs() takes 1 positional argument but 2 were given
#print(my_abs(100,22))

my_abs('')

#abs('a')