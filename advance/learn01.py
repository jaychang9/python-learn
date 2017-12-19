L = ['Michael','James','Jay','Lily','Jack']

print(L[2:4])


print(L[-2:])



print(L[-1:])


L = list(range(1,101))


print(L[:10])

print(L[-10:])

#print(L[0:10:2])
print(L[:10:2])

print(L[-10::2])

print(L[::5])


T = tuple(range(1,101))

print(T[-10:])


print(T[-10::3])


S = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print(S[-2:])


print(S[::2])


def trim(str):
    while str[:1] == ' ':
        str = str[1:]
    while str[-1:] == ' ':
        str = str[:-1]
    return str


# def trim(str):
#     if str == '':
#         return ''
#     i = 0
#     length = len(str)
#     while i <= length -1 and str[i] == ' ':
#         i += 1
#     j = length - 1
#     while j >= 0 and str[j] == ' ':
#         j -= 1
#     if i > j:
#         return ''
#     if j <= length - 1 and str[j] != ' ':
#         return str[i:j+1]
#     return str[i:j]

print(trim('hello  '))
print(trim('  hello '))
print(trim(''))
print(trim('   '))
#测试:
if trim('hello  ') != 'hello':
    print('测试失败1!')
elif trim('  hello') != 'hello':
    print('测试失败2!')
elif trim('  hello  ') != 'hello':
    print('测试失败3!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败4!')
elif trim('') != '':
    print('测试失败5!')
elif trim('    ') != '':
    print('测试失败6!')
else:
    print('测试成功7!')

