# -*- coding: utf-8 -*-

# 命名关键字参数,入参列表中需要有*隔开

def person(name,age,*,city,sex):
    print('name:%s,age:%s,city:%s,sex:%s' % (name,age,city,sex))

person('Jay',31,city='Hangzhou',sex='Male')


# 如果已经有可变参数,就不需要有*隔开了

def person1(name,age,*jobs,city='Beijing',sex):
    print('name:%s jobs:%s age:%s city:%s sex:%s' % (name,jobs,age,city,sex))


person1('Jay',31,['Java Engineer','DBA','DevOps'],city='Hangzhou',sex='Male')


# 使用缺省city值
person1('Jay',31,['Java Engineer','DBA','DevOps'],sex='Male')


# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

def f1(a,b,c=0,*args,**kw):
    print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)

f1(1,2)

f1(1,2,3)

f1(1,2,3,'arg1','arg2')

f1(1,2,3,'arg1','arg2',city='Hangzhou')


t = (1,2,3,'arg1','arg2')
kw = {'k1':'v1','k2':'v2'}

f1(*t,**kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

extra = {'k1':'v1','k2':'v2'}

f2('a','b',3,d='d',**extra)

#所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。


def product(a,b=1,*args):
    result = a * b
    for n in args:
        result *= n
    return result



# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')

