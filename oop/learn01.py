#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Student(object):

    def __init__(self,name,score):
        self.__name = name
        self.age = 30
        self.__score = score

    def set_score(self,score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def print_score(self):
        print('name:%s,score:%s' % (self.__name,self.__score))





lily = Student('lily',80)

james = Student('james',90)

lily.print_score()

james.print_score()

james.set_score(88)
james.print_score()

print('%s %s' % (lily._Student__name,james._Student__name))

# setattr(lily,'age',30)
print(hasattr(lily,'age'))
print(getattr(lily,'age'))
print(getattr(lily,'xxx',404))

fn = getattr(lily,'set_score')

fn(99.999999)

lily.print_score()