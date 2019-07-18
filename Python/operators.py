# if 0:
#     print("True\n")
# print("All is ОРКИ")

# if 1:
#     print("True\n")
# print("All is ОРКИ")

# if 1:
#     print("True")
#     print("All is ОРКИ") 

# num = input("Угадай Test, падла: ")

# if num == "Test":
#     print("пошёл\n")
#     print("в жопу)") 

# num = input("Угадай Test, падла: ")

# if num != "Test":
#     print("пошёл\n")
#     print("в жопу)") 

# num =  input("Введите число плз меньше -10: ")

# if int (num) > 0:
#     print("Не то наклыкал")
# elif int (num) < -10:    
#     print("Опять не то наклыкал, меньше -10")
# print("Всё норм") 


# num =  input("Введите число плз : ")

# if int (num) > 0:
#     print("Вы ввели число больше 0")
# elif int (num) == -10:    
#     print("Опять не то наклыкал, меньше -10")
# elif int (num) == -12:    
#     print("Опять не то наклыкал, меньше -10")
# else:
#     print ("вы ввели число меньше 0 и больше  -0")
# print("Всё норм") 

num =  input("Введите число плз : ")

if int (num) > 0:
    if int (num) > 10:
       print("Вы ввели число больше 10")
       if int (num) > 50:
           print ("Вы ввели число болье 50")
    else:   
         print("Вы ввели число больше 0")
elif int (num) == -10:    
    print("Опять не то наклыкал, меньше -10")
elif int (num) == -12:    
    print("Опять не то наклыкал, меньше -10")
else:
    print ("вы ввели число меньше 0 и больше  -0")
print("Всё норм") 

name = input ("Введите Test. Если нет, то не вводи")
A = 'Yes' if name != "Test" else 'No'
print (A)