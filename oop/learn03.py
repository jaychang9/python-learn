#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
    def __init__(self,name):
        self.__name = name

    def get_name(self):
        return self.__name


    def set_name(self,name):
        self.__name = name

    def run(self):
        print('Animal %s is running...' % self.__name)


class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)

    def eat(self):
        print('Dog like eatting meal...')

class Cat(Animal):
    def __init__(self,name):
        super().__init__(name)

    def eat(self):
        print('Cat like eatting fish...')


class Husky(Dog):
    def __init__(self,name):
        super().__init__(name)

    def __len__(self):
        return 10

a = Animal('a')
d = Dog('d')
c = Cat('c')
h = Husky('h')

a.run()
d.run()
c.run()
h.run()

d.eat()

c.eat()

print(isinstance(a,Animal))
print(isinstance(c,Animal))
print(isinstance(d,Animal))
print(isinstance(c,Cat))
print(isinstance(d,Dog))


print(type(a))
print(type(c))
print(type(d))
print(type(h))

print(isinstance(h,Husky))
print(isinstance(h,Dog))
print(isinstance(h,Animal))

print('len method %s ' % len(h))


print(hasattr(h,'__name'))

