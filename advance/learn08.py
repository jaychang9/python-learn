# -*- coding: utf-8 -*-
import functools

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}



def str2int(s):
    def char2num(x):
        return DIGITS.get(x)
    def fn(x,y):
        return x * 10 + y
    return functools.reduce(fn,map(char2num,s))


r = str2int('123456')

print(r)


def str2int2(s):
    d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    def char2num(x):
        return DIGITS.get(x)
    return functools.reduce(lambda x,y: x*10+y,map(char2num,s))


r = str2int2('1234446')

print(r)