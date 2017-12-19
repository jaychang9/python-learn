# -*- coding: utf-8 -*-

def fabonacci(max):
    L,i = [1],1
    while i <= max:
        if i >= 3:
            j,a,b = 1,1,L[1]
            while j < i - 1:
                L[j] = a + b
                a, b = b, L[j + 1]
                j += 1
        print(L)
        L.append(1)
        i += 1

fabonacci(10)


