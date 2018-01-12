# -*- coding: utf-8 -*-

f = open('E:\\temp\\develop.txt','r')

l = f.readline()

print(l)

l = f.readline()

print(l)

for l in f.readlines():
    print(l.strip())


img = open('E:\\temp\\截图\\virtualbox网络配置\\1.png','rb')

r = img.read()

print(r)