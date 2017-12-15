# -*- coding: utf-8 -*-
import cmath

def quadratic(a,b,c):
    r1 = (-b + cmath.sqrt(b*b-4*a*c)) / 2*a
    r2 = (-b - cmath.sqrt(b*b-4 * a * c)) / 2 * a
    return r1,r2


# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')