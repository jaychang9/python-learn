
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    __slots__ = ('__name','name','age')
    count = 0

    def __init__(self,name):
        self.__name = name
        Student.count += 1


a = Student('a')
b = Student('b')
# a.xx = 'xx'
print(a.count)

