# Задание 1

# def fizzbuzz(number):
#     if number % 3 == 0 and number % 5 == 0:
#         return "FizzBuzz"
#     elif number % 3 == 0:
#         return "Fizz"
#     elif number % 5 == 0:
#         return "Buzz"
#     else:
#         return number
#
# for number in range(1, 100):
#     print(fizzbuzz(number))


# Задание 2
# решение 1
# s = []
# for i in range(18, 1, -4):
#     s += [i]
# print(s)
# решение 2
# s = []
# for i in range(18, 1, -4):
#     s.append(i)
# print(s)

# Задание 3
# Читать внимательно условие! Надо просто вывести элементы, а не создавать список
# lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
# lst1 = []
# sum = 0
# for item in lst:
#     if item < 30 and item % 3 == 0:
#         lst1.append(item)
#     else:
#         sum += item
# print(lst1, f"Сумма: {sum}")

# Корректное решение
# lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
# sum = 0
# for item in lst:
#     if item < 30 and item % 3 == 0:
#         print(item)
#     else:
#         sum += item
# print(f"Сумма: {sum}")


# Задание 4
# def calc(a, b, operation):
#     if operation == "+":
#         return a + b
#     elif operation == "-":
#         return a - b
#     elif operation == "*":
#         return a * b
#     elif operation == "/":
#         if b != 0:
#             return a / b
#         else:
#             return ("На '0' делить нельзя")
#     else:
#         return ("Операция не поддерживается")
#
#
# print(calc(5, 5, "+"))
# print(calc(5, 5, "-"))
# print(calc(5, 10, "-"))
# print(calc(5, 5, "*"))
# print(calc(5, 5, "/"))
# print(calc(5, 0, "/"))

# Задание 5
#решение 1
# for i in range(1, 200):
#     if i == 139:
#         break
#     else:
#         i % 2 != 0
#         print(i)

#решение 2
#Не понятно почему применяем только elif, и не работает с else!!!!
# s = [1, 2, 355, 8, 9, 139, 5, 7, 4]
#
# for i in s:
#     if i == 139:
#         break
#     elif i % 2 != 0:
#         print(i)
#     # else:
#     #     i += [1]

# Задание 6

# def multi_table(num):
#     st = str()
#     for x in range(1, 11):
#         z = num * x
#         st += '{} * {} = {}\n'.format(x, num, z)
#     return st
#
# print(multi_table(5))

# Задание 7

# def is_isogram(string):
#     string = string.lower()
#     for letter in string:
#         if string.count(letter) > 1: return False
#     return True
# print(is_isogram("Dermatoglyphics"))
# print(is_isogram("ABBA"))

# Задание 8
#Решение 1
# def find_smallest_int(arr):
#     smallest = arr[0]
#     for i in range(0, len(arr)):
#         if arr[i] < smallest:
#             smallest = arr[i]
#     return smallest
# print(find_smallest_int([2, 345, 43, -1]))

#решение 2

# mas = [2, 345, 43, -1]
# maximum = mas[0]
# for i in range(1, len(mas)):
#     if mas[i] > maximum:
#         maximum = mas[i]
# print(maximum)

#решение 3

# def find_smallest_int(arr):
#     return min(arr)                     # max(arr)
#
# print(find_smallest_int([2, 345, 43, -1]))

# Задание 9

# def repeatStr(repeat, string):
#     return repeat * string
# print(repeatStr(6,"HI! "))

# Задание 10

# def bool_to_word(boolean):
#     if bool:
#         return "Yes"
#     else:
#         return "No"
# print(bool_to_word(True))

# Задание 11

# def descending_order(num):
#     return int("".join(sorted(str(num), reverse=True)))
# print(descending_order(123456))

# Задание 12

def add_or_even(arr):
    if sum(arr) % 2 == 0:
        return 'even'
    else:
        return 'odd'
print(add_or_even([0, 1, 4]))