# def func(x, a):
#     return x+a
# print(func(23, 12))

# def func(x, a):
#     res = x+a
#     return res
# print(func('hi ', 'world'))

# def func (x):
#     def add (a):
#         return x + a
#     return add
# test = func(100)
# print(test(200))


# def func ():
#     pass # не возвращает ничего
# print(func)

# def func(r, w, y=2):
#     res = r + w
#     res *= y
#     return res

# print(func(2,4,3))

# def func(**args):
#     return args

# print(func(a=23,n=56,o=999))

# def func(**args):
#     return args

# print(func(short='dict',longer='dictionary`'))

def func(**args):
    return args

print(func(short='dict',longer='dictionary'))

add = lambda x,y: x*y
print(add(1,5))
print(add('Очко',2))

print((lambda x,y: x*y)(2,6))

fun = lambda *args: args
print(fun(2,56,78.65))