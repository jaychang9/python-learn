# -*- coding: utf-8 -*-

def fact(n=1):
    if n > 1:
        return fact(n-1)*n
    else:
        return 1


print(fact(998))



def fact_p(a,b):
    if a == 1:
        return b
    else
        return fact_p(a,a*b)


def fact1(n=1):
   return fact_p()


