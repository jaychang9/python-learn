# -*- coding: utf-8 -*-

print("hello\\ \npython\tyeah!")
print("**************************")
# 不转义
print(r"hello\\ \npython\tyeah!")
# 多行可以使用'''xxxxxxxxx''' (若不想被转义使用r'''xxxxxxxx''')
print("**************************")
print('''"hello\\ \npython\tyeah!"''')
print("**************************")
print(r'''"hello\\ \npython\tyeah!"''')


age = int(input('input age:'))

if age >= 18:
    print('you are a child\n')
elif age > 3:
    print('you are a teenage\n')
else:
    print('you are a child\n')