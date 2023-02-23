# Задание 1

# def m1(a, b):
#     c = a * b
#     if c > 1000:
#         return a + b
#     return c
# assert (m1(20, 30) == 600)
# assert (m1(40, 30) == 70)
# assert (m1(20, 30) == 500)

# Задание 2
# решение 1
# def m2(input_str):
#     size = len(input_str)
#     output_list = []
#     for i in range(0, size, 2):
#         output_list.append(input_str[i])
#     return output_list
# assert(m2('python1') == ['p', 't', 'o', '1'])

# решение 2

# def m2(input_str):
#     x = list(input_str)
#     return x[0::2]
# assert (m2('python1') == ['p', 't', 'o', '1'])

# Задание 3
# решение 1
# def m3(input_str):
#     size = len(input_str)
#     output_str = []
#     for i in range(size):
#         output_str.append(input_str[-i - 1])
#     return ''.join(output_str)
# # print(m3('abc') == 'cba')
# assert (m3('abc') == 'cba')

# решение 2
# def m3(input_str):
#     return input_str[::-1]
# assert (m3('abc') == 'cba')

# Задание 4

# import random
# lot_ticket_list = []
# for i in range(1000):
#     lot_ticket_list.append(random.randrange(10**9, 9999999999))
# win = random.sample(lot_ticket_list, 5)
# print('winners are', win)

# Задание 5

# import random
#
# name = 'skillfactory'
# char = random.choice(name)
# print(char)

# Задание 6

# import random
# import string
#
# def randomPasswor() -> str:
#     randomSource = string.ascii_letters + string.digits + string.punctuation
#     password = random.sample(randomSource, 6)
#     password += random.sample(string.ascii_uppercase, 2)
#     password += random.sample(string.digits, 1)
#     password += random.sample(string.punctuation, 1)
#
#     pass_list = list(password)
#     random.SystemRandom().shuffle(pass_list)
#     password = ''.join(pass_list)
#
#     return password
# print(randomPasswor())

# Задание 7

# list1 = ['M', 'na', 'i', 'Vasi']
# list2 = ['y', 'me', 's', 'liy']
# list3 = [i+j for i, j in zip(list1, list2)]
# print(list(zip(list1, list2)))
# print(list3)

# Задание 8

# set1 = {'a', 'b', 'c'}
# list1 = ['d', 'c', 'f']
# set1.update(list1)
# print(set1)

# Задание 9 Не работает код, strptime не относится к datetime???

# import datetime
# date_string = 'Mar 14 2022 8:41PM'
# # привести к формату 2022-03-14 20:41:00
# datetime_obj = datetime.strptime(date_string, '%b %d %Y %I:%M:%p')
# print(datetime_obj)

# Задание 10

# def f1(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum
# assert(f1(1, 2, 3) == 6)
# assert(f1(4, 5) == 9)

# Задание 11

# def f2(name, salary=4000):
#     print('Name:', name, ",", "salary:", salary)
# f2("Ivan", 9000)
# f2("Nikolay")

# Задание 12

# tuple = ('red', [1, 2, 3], (6, 8, 9))
# print(tuple[1][2])

# Задание 13
#Пирамида из чисел

# def f3(row):
#     for i in range(1, row+1):
#         for j in range(1, i+1):
#             print(j, end=' ')
#         print('')
# f3(10)

# Задание 14

# l1 = [3, 6, 9, 12, 15, 18, 21]
# l2 = [4, 8, 12, 16, 20, 24, 28]
# odd_elem = l1[1::2]             #выбираем нечетный элемент
# even_elem = l2[0::2]            #выбираем четный элемент
#
# result = []
# result.extend(odd_elem)
# result.extend(even_elem)
# print(result)

# Задание 15

# set1 = {1,2,3}
# set2 = {1,2,3,4,5,6}
# if set1.issubset(set2):
#     print('set1 is subset set2')
# if set2.issubset(set1):
#     print('set2 is subset set1')

# Задание 16
# Код не работает почему-то

# d1 = {'key': ['a', 'b', {'key': ['n', 'e']}]}
# d1['key2'] = {'c', 'd'}
# d1['key2'].append({'key2:['e','f']})
# print(d1)
