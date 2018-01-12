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
    else:
        return fact_p(a,a*b)


def fact1(n=1):
   return fact_p()





def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)

move(21,'A','B','C')