i = 1000
while i > 100:
    print (i)
    i /= 2

# for j in 'Хаюхай, Я ИванГай':
#     if j == 'ю':
#         continue
#     print(j * 4, end = '') 
    

# for j in 'Хаюхай, Я ИванГай':
#     if j == 'ю':
#         break
#     print(j * 4, end = '') 
    
for j in 'Хаюхай, Я ИванГай':
    if j == 'з':
        break
    # print(j * 4, end = '') 
else:
    print("ОпОпОп, нет быквы 'з'")
