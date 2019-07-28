# a = set("hello")
# print (type(a))
# print(a)

# a = {i**2 for i in range(20)}
# print (type(a))
# print(a)

# a = set("Hello")
# frozenset("Qwerty")
# a.add(1)
# print(a)

# a = ['r','s','w','a','t','t']
# print(a)
# print(set(a))

# a = {32,45,22,12.22,11}
# x = 45
# print(x in a)

a = {32,45,22,12.22,11}
x = {67, 12, 91, 22, 134,45}
# print(a.isdisjoint(x))
# a.intersection_update(x) # пересечения
# a.difference_update(x) # пересечения множеств
# a.symmetric_difference_update(x) # не встречающиеся в обоих множества
# a.remove(32) # и так понятно
# a.discard(32) # удаляет если нашёл, если не нашёл то без ошибки
a.pop() # удаляет рандомный элемент
a.clear() # и так понятно
# a.update(x) # объеденяет множества
print(a)