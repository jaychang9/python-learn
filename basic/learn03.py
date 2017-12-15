# -*- coding: utf-8 -*-

sum = 0

for a in list(range(1,101)):
    # print(a)
    sum += a

print(sum)

sum = 0
index = 99
array = list(range(1,101))
while index >= 0:
    if index % 2 == 0:
        index = index - 1
        continue
    sum = sum + array[index]
    index = index - 1
print(sum)


print('END')