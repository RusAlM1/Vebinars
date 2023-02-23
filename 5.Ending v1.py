# Задание 1
# Ввести ФИО, вывести фамилия+инициалы

# fio = input("ВВедите ФИО: ")
# f, i, o = fio.split()
# # решение вариант 1
# ans1 = f + " " + i[0] + ". " + o[0] + "."
# print(ans1)
# # решение вариант 2
# ans2 = f"{f.capitalize()} {i[0].upper()}. {o[0].upper()}." #capitalize - первую букву делает заглавной; upper - делает заглавной
# print(ans2)

# Задание 2
# def check_date(s_date):
#     if len(s_date.split("-")) != 3:
#         return False
#     year, month, day = s_date.split("-")
#     if len(year) != 4 or len(month) != 2 or len(day) != 2:
#         return False
#     if not (year.isdigit() and month.isdigit() and day.isdigit()): # isdigit - проверяет что данные являются числом
#         return False
#     year, month, day = int(year), int(month), int(day)
#     if 1000 <= year <= 3000 and 1 <= month <= 12 and 1 <= day <= 31:
#         return True
#     else:
#         return False
# print(check_date("2023-02-14"))
# print(check_date("202302-14"))
# print(check_date("2023-2-14"))
# print(check_date("2023-0w-14"))
# print(check_date("2023-13-14"))
# print(check_date("2023-02-44"))

# Задание 3
# def ask_date():
#     print("Введите дату: ")
#     date = None
#     while date is None:
#         temp = input()
#         if check_date(temp):
#             return temp
#         else:
#             print("Введена некорректная дата")
#     return date

# Задание 4
# Подсчитать кол-во символов встречающихся в словаре

# решение 1
# def list_stat(A):
#     stat = {}
#     for num in A:
#         if num in stat:
#             stat[num] += 1
#         else:
#             stat[num] = 1
#     return stat

# решение 2

# def list_stat2(A):
#     stat = {}
#     for num in set(A):
#         stat[num] = A.count(num)
#     return stat

#Задание 5
#Решение 1. Функция работает в паре с решением задания 4. Иначе выдает ошибку
# def list_sort(A):
#     stat = list_stat(A)
#     keys = list(stat.keys())
#     keys.sort(key=lambda x: stat[x])
#     print(keys)
# list_sort([1, 2, 1, 1, 2, 3, 4, 6, 4, 4, 10])

#Решение 2. Функция работает в паре с решением задания 4. Иначе выдает ошибку
# def list_sort(A):
#     stat = list_stat(A)
#     items = list(stat.items())
#     items.sort(key=lambda x: x[1])
#     print(items)
# list_sort([1, 2, 1, 1, 2, 3, 4, 6, 4, 4, 10])

# Задание 6
# Записать фаил
# import json
# def save_info(info):
#     with open("info.json", "w") as f:  # open ("") в кавычках прописываем имя файла
#         json.dump(info, f)
#
# a = [
#     {1:2},
#     {"b":"c"},
#     "123123",
#     132
# ]
# save_info(a)

# Прочесть (открыть) фаил

# import json
#
# def load_info():
#     with open("info.json") as f:
#          info = json.load(f)
#     return info
# info = load_info()
# print(info)

# Задание 7
# Функция которая принимает три даты и возвращает True если даты в порядке возрастания

import datetime
date_1 = "2023-02-14"
date_2 = "2023-02-15"
date_3 = "2023-03-07"
def compare_dates(date_1, date_2, date_3):
    date_1 = datetime.date.fromisoformat(date_1)
    date_2 = datetime.date.fromisoformat(date_2)
    date_3 = datetime.date.fromisoformat(date_3)
    return date_1 <= date_2 <= date_3

print(compare_dates(date_1, date_2, date_3))