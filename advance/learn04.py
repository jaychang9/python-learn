# --*-- encoding = utf-8 --*--

def fibonacci(n):
    arr,i = [1,1],2
    while i < n:
        arr.append(arr[i-1]+arr[i-2])
        i += 1
    return arr

def fabonacci2(n):
    i,a,b = 0,0,1
    while i < n:
        print(b)
        a,b = b,a+b
        i += 1


def fabonacci3(n):
    i,a,b = 0,0,1
    while i < n:
        yield b
        a,b = b,a+b
        i += 1

print(fibonacci(10))

fabonacci2(10)

g = fabonacci3(10)

print('*********************')

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print('*********************')

g = fabonacci3(10)

for x in g:
    print(x)


print('*********************')

def odd():
    print('step1')
    yield 1
    print('step2')
    yield 2
    print('step3')
    yield 3
    return 'done'

g = odd()

print(next(g))
print(next(g))
print(next(g))

print('*****************')
g = odd()
for x in g:
    print(x)


print('*****************')
g = odd()
while True:
    try:
        x = next(g)
        print('x:',x)
    except StopIteration as e:
        print('Generator value :',e.value)
        break


