#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Jay Chang'

def _private1(name):
    return 'Hello,%s' % name

def _private2(name):
    return 'Hi,%s' % name

def greeting(name):
    if len(name) >= 3:
        print(_private1(name))
    else:
        print(_private2(name))
