# Кортежи нередактируемы
# a = (43,22,34,11,228, 'a')
# b = [43,22,34,11,228, 'a']

# a[0] = 34 - так не прокатит

# print(a.__sizeof__())
# print(b.__sizeof__())

# a = tuple("Hello World") # делит строку на элементы
# print(a)

# a = ("Hello World") # делит строку на элементы
# print(a)

# a = "Hello World", "34", 228 #запятая решает кортеж ли это, скобки - нет
# print(a)

a = ("Hello World", "34", 228) 
print(a)

print (a.count (228))

