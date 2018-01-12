# -*- coding: utf-8 -*-

import functools

L = list(range(1,11))
r = filter(lambda x:x % 2 == 0 ,L)
print(list(r))


r = list(map(lambda x: x * x,list(filter(lambda x:x % 2 == 0,L))))

print(r)


r = functools.reduce(lambda x,y:x+y,list(map(lambda x: x * x,list(filter(lambda x:x % 2 == 0,L)))))

print(r)


L = ['A',' ',None,' ADF ',' ']

r = list(filter(lambda x : x and x.strip(),L))

print(r)