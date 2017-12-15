# -*- coding: utf-8 -*-

def show(name,age,**keyword):
    if 'city' in keyword:
        print('keyword has city key')
    print('name:',name,'age:',age,'other:',keyword)

show('Micheal',31,city='Beijing',sex='Male')


extra={'city':'Beijing','sex':'Male'}

show('Micheal',31,city=extra['city'],sex=extra['sex'])


show('Micheal',31,**extra)