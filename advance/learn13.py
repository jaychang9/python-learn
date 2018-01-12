# -*- coding: utf-8 -*-

def f(*args):
    L = []
    for i in args:
        def ff():
            return i*i
        L.append(ff)
    return L

f1,f2,f3 = f(1,2,3)
print('%d %d %d' % (f1(),f2(),f3()))

def f2(*args):
    L = []
    for i in args:
        def ff(x):
            def g():
                return x*x
            return g
        L.append(ff(i))
    return L

f1,f2,f3 = f2(1,2,3)
print('%d %d %d' % (f1(),f2(),f3()))


