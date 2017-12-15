# -*- coding: utf-8 -*-

def power(x,n = 2):
    while n > 1:
        x = x * x
        n = n - 1
    return x

print(power(3,2))

def add_append(L = None):
     if L == None:
         L = []
     L.append('END')
     return L

list = []
print(add_append(list))
print(add_append(list))