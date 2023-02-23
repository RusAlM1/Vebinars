#Задание 1 вар 1

# a = int(input('введите число от 1 до 99: '))
# digit1 = a % 10
# digit2 = a // 10
# s = digit1 + digit2
# print(s)

#вар 2

# n = int(input('введите число: '))
# s=0
# for digit in str(n):
#     s +=int(digit)
# print(s)

#вар 3
# digit = list(str(n))
# s = sum(map(int, digit))
# print(s)

#Задание 2
# вар 1

# import math
# a = int(input("введите число а: "))
# b = int(input("введите число b: "))
# ans = math.sqrt(a ** 2 + b ** 2)
# print(ans)

# вар 2

# a = int(input("введите число а: "))
# b = int(input("введите число b: "))
# ans = (a ** 2 + b ** 2) ** 0.5
# print(ans)

# вар 3
# import math
# a = int(input("введите число а: "))
# b = int(input("введите число b: "))
# ans = math.hypot(a, b)
# print(ans)

#Задание 3
#вариант 1

# email = "admin@ya.ru"
# at_index = None
# for i in range(len(email)):
#     if email[i] == "@":
#         at_index = i
# ans = email[at_index + 1:]
# print(ans)

#вариант 2

# s = "admin@ya.ru"
# ans = s[s.find('@')+1:]
# print(ans)

#вариант 3

# email = "admin@ya.ru"
# s = email.index("@")
# domen = email[s + 1:]
# print(domen)

# вариант 4

# email = "admin@ya.ru"
# domen = email.split('@')[1]
# print(email.split('@'))
# print(domen)

#Задание 4
#вариант 1

# A = [1, 2, 3, 4, 5, 6, 7, 9, 12, 12312]
# s = 0
# for i in range(len(A)):
#     if i % 3 == 0:
#         s += A[i]
# print(s)

#вариант2

# A = [1, 2, 3, 4, 5, 6, 7, 9, 12, 12312]
# s = 0
# for i, elem in enumerate(A):
#     if i % 3 == 0:
#         s += elem
# print(s)

#вариант3

# A = [1, 2, 3, 4, 5, 6, 7, 9, 12, 12312]
# s = sum(elem for i, elem in enumerate(A) if i % 3 == 0)
# print(s)

#вариант4
# A = [1, 2, 3, 4, 5, 6, 7, 9, 12, 12312]
# new_A = A[::3]
# s = sum(new_A)
# print(new_A)
# print(s)

#Задание 5
#вариант 1

# A = [1, 2, 3, 4, 5, 6, 7]
# first = A.pop()
# A.insert(0, first)
# print(A)

#вариант 2

# m = [1, 2, 3, 4, 5]
#
# x = 2
# for i in range(x):
#     a1 = m.pop()
#     m.insert(0, a1)
# print(m)

#вариант 3

# A = [1, 2, 3, 4, 5, 12, 15]
#
# n = 3 # В таком коде сдвиг надо брать по длине списка. Если в списке 7 значений - то и n дю быть не больше
# B = A[-n:] + A[:-n]
# print(B)

#Задание 6
#вариант 1

# A = [1, 2, 3, 4, 5, 6, 7]
# min_elem = None
# for elem in A:
#     if min_elem == None or min_elem > elem:
#         min_elem = elem
# print(min_elem)

#вариант 2

# A = [1, 2, 3, 4, 5, 6, 7]
# min1 = A.pop(A.index(min(A)))
# min2 = A.pop(A.index(min(A)))
# min3 = A.pop(A.index(min(A)))
# print(min2, min3)

#вариант 3

# A = [1, 1, 1, 2, 3, 4, 5, 6, 7]
# min1 = min(A)
# A = list(filter(lambda elem: elem != min1, A))
# # A.remove(min1)
# min2 = min(A)
# A.remove(min2)
# min3 = min(A)
#
# print(min2, min3)

#вариант 4

# A = [1, 4, 5, 2, 6, 7, 3]
# A.sort()
# print(A[1], A[2])

#Задание 7
#вариант 1

# s = "12412541234"
# n = 7
# ans = 0
# for i in range(len(s)):
#     ans += int(s[-i]) * n ** i
# print(ans)

#вариант 2

# n = 7
# s = "12412541234"
#
# ans = 0
# for digit in s:
#     ans *= n
#     ans += int(digit)
# print(ans)

#Задание 8
#вариант 1

# A = [[1, 2], [3, 4, 5], [6], [7, 8, 9, 10], [11], [12, 13, 14]]
# B = []
# for elem in A:
#     for i in elem:
#         B.append(i)
# print(B)

#вариант 2
# A = [[1, 2], [3, 4, 5], [6], [7, 8, 9, 10], [11], [12, 13, 14]]
# B = []
# for elem in A:
#     B.extend(elem)
# print(B)

#вариант 3
# A = [[1, 2], [3, 4, 5], [6], [7, 8, 9, 10], [11], [12, 13, 14]]
# B = []
# for elem in A:
#     B += elem
# print(B)

#вариант 4
# A = [[1, 2], [3, 4, 5], [6], [7, 8, 9, 10], [11], [12, 13, 14]]
# B = sum(A, [])
# print(B)

#Задание 9
#вариант 1

# text = "Какой-то линейный текст для подсчета статистики"
# unsymb = set(text)
# for symbol in unsymb:
#     symb_count = text.count(symbol)
#     print(f"'{symbol}' - {symb_count}")

#вариант 2
# text = "Какой-то линейный текст для подсчета статистики"
# stat = {}
# for s in text:
#     if s in stat:
#         stat[s]+=1
#     else:
#         stat[s]=1
# for s, count in stat.items():
#     print(f"Символ '{s}' встертился {count} раз")

#вариант 3
# from collections import Counter
# text = "Какой-то линейный текст для подсчета статистики"
# stat = Counter(text)
# for s, count in stat.items():
#      print(f"Символ '{s}' встертился {count} раз")

#Задание 10
#вариант 1

# n = 23
# isprime = True
# for div in range(2, n):
#     if n % div ==0:
#         isprime = False
# print(isprime)

#Задание 11
#Пользователь ввсел строку. написать код который удвляет каждое второе слово

#вариант 1

# a = input("Введитe текст: ")
# words = a.split()
# s = ""
# for i in range(len(words)):
#     if i % 2 == 0:
#         s += words[i]
#         s += " "
# print(s)

#вариант 2

# a = input("Введитe текст: ")
# words = a.split()
# s = ""
# for i, word in enumerate(words):
#     if i % 2 == 0:
#         s += word
#         s += " "
# print(s)

#вариант 3

# a = input("Введитe текст: ")
# words = a.split()
# even_words = words[::2]
# s = " ".join(even_words)
# print(s)

#Подзадание: убрать знаки пунктуации

# import string
# a = "Строка, в которой есть несколько слов (!)"
# words = a.split()
# words = [word.strip(string.punctuation) for word in words]
# words = [word for word in words if word]
# print(words)

# или упростим:

# import string
# a = "Строка, в которой есть несколько слов (!)"
# for s in string.punctuation:
#     a = a.replace(s, "")
# words = a.split()
# print(words)

#Задание 12
# Ввести с клавиатуры число. вывести число в двоичной системе исчисления.

# num = int(input("Введите число: "))
# ans = ""
# while num:
#     if num % 2 == 0:
#         ans = "0" + ans
#     else:
#         ans = "1" + ans
#     num = num // 2
# print(ans)

#Вариант 2

# num = int(input("Введите число: "))
# ans = ""
# while num:
#     ans = str(num % 2) + ans
#     num = num // 2
# print(ans)

#Вариант 3

num = int(input("Введите число: "))
ans = bin(num)

print(ans[2:])
