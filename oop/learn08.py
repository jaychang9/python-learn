#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self,name):
        self.__name = name

    @property
    def score(self):
        return self.__score

    @property
    def birth(self):
        return self.__birth

    @birth.setter
    def birth(self,birth):
        self.__birth = birth

    @property
    def age(self):
        return 2017-self.__birth

    @score.setter
    def score(self,score):
        if isinstance(score,int) == False:
            raise ValueError('score must be a integer')
        if score < 0 or score > 100:
            raise ValueError('score must between 0 and 100')
        self.__score = score


    def __str__(self):
        return 'Student Object Haha '+self.__name+' '+int.__str__(self.__birth)






a = Student('a')
a.score = 11

# ValueError: score must between 0 and 100
# a.score = 101

a.birth = 1987
# a.age = 20
print('birth:%s,age:%s,score:%s' % (a.birth,a.age,a.score))

print(a)