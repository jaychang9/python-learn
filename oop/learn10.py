#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
    def __init__(self):
        print('Animal init')


class Mammal(Animal):
    def __init__(self):
        super().__init__()
        print('Mammal init')



class Bird(Animal):
    def __init__(self):
        super().__init__()
        print('Bird init')

class FlyableMixIn(object):
    def __init__(self):
        print('FlyMixIn init')

    def fly(self):
        print('flying...')


class RunableMixIn(object):
    def __init__(self):
        print('RunMixIn init')

    def run(self):
        print('running...')


class Dog(Mammal,RunableMixIn):
    def __init__(self):
        super().__init__()
        print('Dog init')

class Bat(Mammal,FlyableMixIn):
    def __init__(self):
        super().__init__()
        print('Bat init')

class Ostrich(Bird,RunableMixIn):
    def __init__(self):
        super().__init__()
        print('Ostrich init')

class Parrot(Bird,FlyableMixIn):
    def __init__(self):
        super().__init__()
        print('Parrot init')


d = Dog()
b = Bat()
o = Ostrich()
p = Parrot()


d.run()
b.fly()
o.run()
p.fly()