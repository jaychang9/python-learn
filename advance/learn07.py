# -*- coding: utf-8 -*-
import functools
def f(x):
    return x*x


print(list(map(f,[1,2,3,4,5])))

print(list(map(str,[1,2,3,4,5])))

def ff(x,y):
    r = x + y
    print('%d+%d=%d' % (x,y,r))
    return r

print('reduce function result = ',functools.reduce(ff,[1,2,3,4,5]))


def char2num(x):
    d = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    return d.get(x)
def computer(x,y):
    r = x * 10 + y
    print('%d*10+%d=%d' %(x,y,r))
    return r

num = '1581234'

r = functools.reduce(computer,list(map(char2num,num)))

print(r)

