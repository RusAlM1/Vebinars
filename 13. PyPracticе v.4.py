#Задание 1
# num = int(input('введите число: '))
# data = []
# while num != 0:
#     data.append(num)
#     num = int(input('введите число: '))
# data.sort()
# print(data)

#Задание 2

# word = input('введите слово: ')
# data = []
# while word != '':
#     if word not in data:
#         data.append(word)
#     word = input('введите слово: ')
# for item in data:
#     print(item)

#Задание 3

# line = input('введите число: ')
# negatives = []
# zeros = []
# positives = []
#
# while line != '':
#     num = int(line)
#     if num < 0:
#         negatives.append(num)
#     elif num > 0:
#         positives.append(num)
#     else:
#         zeros.append(num)
#     line = input('введите число: ')
#
# negatives.sort()
# zeros.sort()
# positives.sort()
#
# for item in negatives:
#     print(item)
# for item in zeros:
#     print(item)
# for item in positives:
#     print(item)

#Задание 4
#
# num = int(input('введите число: '))
# cnt = 0
# pr = 1
# while num != 0:
#     if num > 0 and num % 2 != 0 and num % 5 == 0:
#         cnt += 1
#     else:
#         num % 5 == 0
#         pr *= num      #Операция "умножение" выполняется не корректно для последовательности 45,40,-25,11,77,8,5,-2,0
#     num = int(input('введите число: '))
# print(cnt)
# print(pr)

#Задание 5

# num = int(input('введите число: '))
# sum = 0
# while num != 0:
#     if num % 2 == 0 and 4 < num < 26:
#         sum += num
#     num = int(input('введите число: '))
# print(sum)

#Задание 6

# num = int(input('введите число: '))
# sum = 0
# cnt = 0
# while num != 0:
#     if num > 0 and num % 8 == 0:
#         sum +=num
#         cnt += 1
#     num = int(input('введите число: '))
# res = sum // cnt                  #Если применить // - получим целочисленное деление (например ответ будет 12)б
# если применим / - деление будет дробное (например ответ будет 12.0)
# print(res)

#Задание 7

# def multi_table(num):
#     st = str()
#     for x in range(1, 11):
#         z = x * num
#         st += '{} * {} = {}\n'.format(x, num, z)
#     return st
#
# print(multi_table(5))

#Задание 8

# def descending_order(num):
#     return int(''.join(sorted(str(num), reverse=True)))
# print(descending_order(42145))
