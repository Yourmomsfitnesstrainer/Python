l = [] # пустой список
lisRandomNum = [1, 56, 'x' , 34, 2.33, ['S', 't', 'r', 'o', 'b']]
print(lisRandomNum)

a = [a + b for a in 'зде' if a != 'н' for b in 'не возр' if b != 'о']
print(a)

lisRandomNum.append(23) # добавляет элемент в конец списка
lisRandomNum.append(11)
b = [34, 67]
lisRandomNum.extend(b) # расшираение списка lisRandomNum списком b
lisRandomNum.insert(1, 56) # вставлят элемент по индексу
lisRandomNum. append(34)
lisRandomNum.remove(34) #Удаляет
lisRandomNum.pop(0) # удаляет элемент по индексу
print(lisRandomNum.index (56)) # выводит индекс 56 в данном случае
print(lisRandomNum.count(34)) # выводит кол-во элементов со значением
# lisRandomNum.sort() # сортирует
lisRandomNum.reverse() # реверс списка
lisRandomNum.clear() # очищает список
print(lisRandomNum)