import math

# print('1-прямоуг, 2-треуг, 3-круг')
# fig = input('выберите фигуру: ')
#
# if fig == "1":
#     a = float(input('a='))
#     b = float(input('b='))
#     print('Площадь: %.2f' % (a * b))
# elif fig == "2":
#     a = float(input('a='))
#     b = float(input('b='))
#     c = float(input('c='))
#     p = (a + b + c) / 2
#     s = math.sqrt(p * (p - a) * (p - b) * (p - c))
#     print('Площадь: %.2f' % s)
#
# elif fig == "3":
#     r = float(input('Радиус круга r= '))
#     print('Площадь %.2f' % (math.pi * r ** 2))
#
# else:
#     print('Ошибка ввода')

# Задание 2
#
# n = int(input('введите трехзначное число: '))
#
# num1 = n % 10
# # print(num1)
# num2 = n % 100 // 10
# # print(num2)
# num3 = n // 100
# # print(num3)
# print('Сумма цифр: ', num1 + num2 + num3)
# print('Произведение цифр: ', num1 * num2 * num3)

# Задание 3
# a = int(input('a='))
# b = int(input('b='))
# c = int(input('c='))
#
# m = max(a, b, c) # Либо решить через условие If m< b m=b if m<c m=c
# print(m)

# Задание 4
# a = int(input('a='))
# b = int(input('b='))
# c = int(input('c='))
#
# if (b < a < c or c < a < b):
#     print('Среднее: ', a)
# elif (a < b < c or c < b < a):
#     print('Среднее: ', b)
# else:
#     print('Среднее: ', c)

# Задание 5

# from random import random
#
# a = int(random() * 100)
# b = int(random() * 100)
# if a % 2 and b % 2 or a % 2 == 0 and b % 2 == 0:
#     a += 1
# print(a, b)
# if a % 2:
#     print(a)
# else:
#     print(b)

# Задание 6
# import random
#
# num = random.randint(1, 100)
# while True:
#     print('Угадайте число от 1 до 100')
#     guess = int(input('Введите число: '))
#     if guess == num:
#         print('Правильно!')
#         break
#     elif guess < num:
#         print('Загаданное число больше')
#     elif guess > num:
#         print('Загаданное число меньше')

# Задание 7

# num = int(input('введите целое число: '))
# num1 = 0
#
# while num > 0:
#     digit = num % 10  # получаем последнюю цифру
#     num = num // 10  # удаляем последнюю цифру
#     num1 *= 10
#     num1 += digit
# print('Обратное число: ', num1)

# Задание 8

# a = int(input('введите число: '))
# even = 0
# odd = 0
#
# while a>0:
#     if a%2==0:
#         even+=1
#     else:
#         odd+=1
#     a = a//10
# print('Четных: %d, Нечетных: %d' % (even, odd))

# Задание 10

# n = int(input('введите число: '))
# fact = 1
# while n > 1:
#     fact *= n
#     n -= 1
# print(fact)

# n = int(input('введите число: '))
# fact = 1
# for i in range(2,n+1):
#     fact *= i
# print(fact)

# Задание 11

# for i in range(1, 10):
#     for j in range(1, 10):
#         print(i * j, end="\t")
#     print("\n")

# Задание 12

# lst = []
# for item in range(18, -8, -4):
#     lst.append(item)
# print(lst)

# Задание 13

# lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
# med = 30
# div_num = 3
# sm = 0
# for item in lst:
#     if item < med and item % div_num == 0:
#         print(item)
#     else:
#         sm += item
# print('Сумма: ', sm)

# Задание 14

# lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
# print(lst)
# lst[4] = 189
# print(lst)
# lst.remove(3)
# print(lst)

# Задание 14

# dct = {1: "val1", 2: "val2", 3: "val3"}
# dct["key"] = 12345
# print(dct)

# Задание 19

# def calc(a, b, oper):
#     result = "ошибка ввода"
#     if oper == "++":
#         result = a + b
#     elif oper == "-":
#         result = a - b
#     elif oper == "*":
#         result = a * b
#     elif oper == "/":
#         if b != 0:
#             result = a / b
#         else:
#             result = "Ошибка! на 0 делить нельзя"
#     return result
#
# if __name__ == "__main__":
#     print(calc(30, 15, "+"))
#     print(calc(30, 15, "-"))
#     print(calc(30, 15, "/"))
#     print(calc(30, 0, "/"))
#     print(calc(2, 15, "*"))

# Задание ООП

class Person:
    name = "Ivan."
    age = "25."
    adress = "underBridge."
    def info(self):
        print("Hi, my name is", self.name, " My age", self.age, " I live in", self.adress)
person_1 = Person()
person_1.info()
