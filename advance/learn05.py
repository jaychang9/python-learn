# -*- coding: utf-8 -*-

# 杨辉三角
# i表示第几层
def triangles(n):
    i,L = 1,[1]
    while i <= n:
        j = 1
        if i >= 3:
            a,b,j = L[0],L[1],1
            while j < i - 1:
                L[j] = a + b
                a,b = b,L[j+1]
                j += 1
        print(L)
        L.append(1)
        i += 1



def triangles2(max):
    L=[1]
    i = 1
    while i <= max:
        yield L
        L=[L[i]+L[i+1] for i in range(len(L)-1)]
        print('L',L)
        L.insert(0,1)
        L.append(1)
        i += 1

# g = triangles2(10)
#
# for x in g:
#     print(x)








triangles(10)