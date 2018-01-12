#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):

    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1


a = Student('a')
b = Student('b')
c = Student('c')

print(Student.count)

a.count = 14

print(a.count)
#delattr(a,'count')
del a.count
print(a.count)
print(b.count)
print(c.count)


