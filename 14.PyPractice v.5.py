# myfile = open('hello.txt', 'w') # w = write,  создаем фаил
# myfile = open('hello.txt', 'r') # r = read, читаем созданный ранее фаил
# file = myfile.read()
# print(file)
# myfile.close()


# with open('hello.txt') as f:
#     a = f.readlines()
#     # b = list(map(int, a))             # решение 1
#     b = [int(x) for x in a]             # решение 2
#     print(b)

# Задание 1
# Выдает ошибку, не хватает данных?
# with open('hello.txt') as f:
#     s = f.readlines()
#     a = list(map(int, s))
#     res = []
#     for i in a:
#         if str(i).count('0') >= 2 and i % 7 == 0:
#             res.append(i)
# print(max(res), len(res))

# Задание 2
# Выдает ошибку, не хватает данных?
# with open('hello.txt') as f:
#     s = [int(x) for x in f]
#     res = []
#     for i in range(1, len(s)):
#         if (abs(s[i]) % 10 == 7 or abs(s[i-1]) % 10 == 7) and (s[i] + s[i-1]) % 12 == 0:
#             res.append(s[i] + s[i-1])
# print(len(res), max(res))

# Задание 2

# with open('??????.txt') as f:
#     s = f.readline()
#     m = 1
#     k = 1
#     for i in range(1, len(s)):
#         if s[i] != s[i-1]:
#             k += 1
#             m = max(k, m)
#         else:
#             k = 1
# print(m)

# Задание 3
# Подсчитать кол-во слов

# file = open('???????.txt')
# data = file.read()
# words = data.split()
# print(len(words))
# file.close()

# Задание 4 - JSON

# import json

# data = {
#     "name": "Ivan",
#     "age": 26,
#     "city": "Sarstov"
# }
# with open('data_file.json', 'w') as f:
#     json.dump(data, f)            #сохранили фаил
#
# with open('data_file.json', 'r') as f:
#     data = json.load(f)
#     print(data)           #открыли фаил для чтения
#     print(type(data))


# edibles = ['отбивные', 'пельмени', 'яйца', 'орехи']
# for food in edibles:
#     if food == 'пельмени':
#         print('я не ем пельмени!')
#         break                         # завершение цикла
#         # continue                        # продолжение цикла
#     print('Отлично, вкусные ' + food)
# else:
#     print('Хорошо, что не было пельменей!')
# print('Ужин окончен.')

# word = input('vvedite slova: ')
# list = []
# while word != '':
#     if word not in list:
#         list.append(word)
#     word = input('vvedite slova: ')
# for x in list:
#     print(x)

class Person:
        def sayHello(self, message):
            print(message)
tom = Person()
tom.sayHello('Hello')
