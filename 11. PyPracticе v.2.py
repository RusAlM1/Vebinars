# Задание 1
# a = int(input("Введите число: "))
# if a == 0:
#     print("Нейтральное число")
# elif a % 2 == 0:
#     print("четное число")
# else:
#     print("не четное")

# Задание 2

# letter = input("Введите букву латинского алфавита: ")
# решение 1
# letter = input("Введите букву латинского алфавита: ")
# let = ["a", "e", "i", "o", "u"]
# if letter in let:
#     print("Буква гласная")
# elif letter == "y":
#     print("Буква может быть гласной и согласной")
# else:
#     print("Буква согласная")

# решение 2
# if letter == "y":
#     print("Буква может быть гласной и согласной")
# elif letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
#     print("Буква гласная")
# else:
#     print("Буква согласная")


# Задание 3

# baby_price = 0.0
# teen_price = 14.0
# adult_price = 23.0
# grand_price = 18.0
#
# baby_limit = 2
# teen_limit = 12
# adult_limit = 64
#
# total = 0
#
# line = input("Введите возраст посетителя (пустая строка для окончания ввода): ")
# while line != "":
#     age = float(line)
#     if age <= baby_limit:
#         total += baby_price
#     elif age <= teen_limit:
#         total += teen_price
#     elif age <= adult_limit:
#         total += adult_price
#     else:
#         total += grand_price
#
#     line = input("Введите возраст посетителя (пустая строка для окончания ввода): ")
# print("Сумма посещения зоопарка для этой группы составит: $%2.f" % total)

# Задание 4

# data = []
# a = int(input("Введите число: "))
# while a != 0:
#     data.append(a)
#     a = int(input("Введите число: "))
# data.sort()
# print(data)

# Задание 5

# words = []
# a = input("Введите слово: ")
# while a != '':
#     if a not in words:
#         words.append(a)
#     a = input("Введите слово: ")
# for item in words:
#     print(item)

# Задание 6

# negatives = []
# zeros = []
# positives = []
#
# line = input("Введите возраст посетителя (пустая строка для окончания ввода): ")
#
# while line != "":
#     num = int(line)
#     if num < 0:
#         negatives.append(num)
#     elif num > 0:
#         positives.append(num)
#     else:
#         zeros.append(num)
#     line = input("Введите возраст посетителя (пустая строка для окончания ввода): ")
#
# negatives.sort()
# zeros.sort()
# positives.sort()
#
# print("Введенные числа")
# for n in negatives:
#     print(n)
# for n in zeros:
#     print(n)
# for n in positives:
#     print(n)

# Задание 7

# numbers = [348, 568, 967, 967, 45, 237, 567, 768, 89]
# for x in numbers:
#     if x == 237:
#         break
#     elif x % 2 == 0:
#         print(x)

# Задание 8
# решение 1
# def palindrome(str):
#     return str == ''.join(reversed(str))
# print(palindrome("dgghrk"))

# решение 2
# def palindrome(str):
#     return str == str[::-1]
# print(palindrome("ABBA"))
# print(palindrome("sdht"))

# Задание 9

# def fizzbuzz(num):
#     if num % 3 == 0 and num % 5 == 0:
#         return "fizzbuzz"
#     elif num % 3 == 0:
#         return "fizz"
#     elif num % 5 == 0:
#         return "buzz"
#     else:
#         return num
# for num in range(1, 101):
#     print(fizzbuzz(num))

# Задание 10
# решение 1
# def is_isogram(str):
#     str = str.lower()
#     for letter in str:
#         if str.count(letter) > 1: return False
#     return True
# print(is_isogram("asftko"))

# решение 2
# def is_isogram(str):
#    return len(set(str.lower())) == len(str)
# print(is_isogram("asdfgbhko;"))

# Задание 11
# решение 1
# def smallest(arr):
#     return min(arr)
# print(smallest([2, 34, 5, -1, 365]))

# решение 2

# def smallest(arr):
#     sm = arr[0]
#     for i in range(0, len(arr)):
#         if arr[i] < sm:
#             sm = arr[i]
#     return sm
# print(smallest([2, 34, 5, -1, 365]))

# Задание 12

mas = [3, 5, 67, -9, 34, 21]
maximum = mas[0]
for i in range(1, len(mas)):
    if mas[i] > maximum:
        maximum = mas[i]
print(maximum)
