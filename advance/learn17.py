# -*- coding: utf-8 -*-

import time
import functools

def metric(f):
    def wrapper(*args,**kw):
        start = time.time()
        r = f(*args, **kw)
        print('%s executed %s' % (f.__name__,time.time()-start))
        return r
    return wrapper


@metric
def hello(name):
    time.sleep(0.11)
    print('%s say hello' % name)

hello('jaychang')




# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')


print('*********************')

def log(text = 'default'):
    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kw):
            print('call %s %s' % (f.__name__, text))
            return f(*args, **kw)
        return wrapper
    return decorator

@log('')
def hello(name):
    print('%s say hello' % name)
print(hello.__name__)
hello('jaychang111')