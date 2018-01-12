# -*- coding: utf-8 -*-

import sys
import functools

def log(f):
    def wrapper(*args,**kw):
        print('call %s ' % f.__name__)
        return f(*args,**kw)
    return wrapper

@log
def now():
    print(sys.base_exec_prefix)

print(now)
now()


print('****************')

# def log1(text):
#     def decorator(f):
#         def wrapper(*args,**kw):
#             print('call %s %s' % (f.__name__,text))
#             return f(*args,**kw)
#         return wrapper
#     return decorator
#
# a = log1('haha')
# a(now)()

def log1(text):
    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args,**kw):
            print('call %s %s' % (f.__name__,text))
            return f(*args,**kw)
        return wrapper
    return decorator

@log1('hello jaychang')
def now1():
    print(sys.base_exec_prefix)

print(now1.__name__)
now1()
