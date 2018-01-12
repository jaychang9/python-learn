# -*- coding: utf-8 -*-

def createCounter():
    def f():
        c = 0
        while True:
            c += 1
            yield c
    g = f()
    def counter():
        return next(g)
    return counter


f = createCounter()

print(f())
print(f())
print(f())

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')