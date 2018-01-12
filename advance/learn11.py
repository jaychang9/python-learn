# -*- coding: utf-8 -*-

import functools

def prime(L = []):
    first = L[0]

    def filtrate(x):
        print(x)
        return x % first != 0

    while True:
        L = list(filter(filtrate,L))
        first = L[0]
    return L


r = prime(list(range(2,101)))

print(r)