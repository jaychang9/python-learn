#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import types

def fun():
    pass

print(type(fun) == types.FunctionType)

print(type(abs) == types.BuiltinFunctionType)

d = {'k':'v'}

def fun_g():
    i = 0
    while True:
        if i % 2 == 0:
            yield i
        i += 1

fg = fun_g()

print(type(fg) == types.GeneratorType)
print(type(lambda x:x*x) == types.LambdaType)
print(type(x for x in (1,2,3)) == types.GeneratorType)

print(type((1,2,3)))
print(type([1,2,3]))