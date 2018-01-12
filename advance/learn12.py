# -*- coding: utf-8 -*-

def calc_sum(*args):
    def sum():
        r = 0
        for x in args:
            r += x
        return r
    return sum



f1 = calc_sum(1,2,3,4,5,6,6)

f2 = calc_sum(1,2,3,4,5,6,7)

print(f1)

print(f1())

print(f2)

print(f2())