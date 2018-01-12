#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Fibonacci(object):
    def __init__(self):
        self.__a ,self.__b= 0,1

    def __iter__(self):
        return self

    def __next__(self):
        if self.__a > 1000:
            raise StopIteration('stop')
        self.__a,self.__b = self.__b,self.__a + self.__b
        return self.__a


    def __getitem__(self, n):
        if isinstance(n,int):
            i,a,b = 0,0,1
            while i < n:
                a,b = b,a+b
                i += 1
            return b
        if isinstance(n,slice):
            start = n.start
            stop = n.stop
            L = []
            i,a,b = 0,0,1
            while i < stop:
                a,b = b,a + b
                i += 1
                if i >= start:
                    L.append(b)
            return L

f = Fibonacci()

for x in f:
    print(x)

print(f[0])
print(f[1])
print(f[2])
print(f[3])
print(f[4])
print(f[5])
print(f[6])
print('test slice')
print(f[3:6])