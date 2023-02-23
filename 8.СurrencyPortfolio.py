# Задание
# Приложение по валютному портфелю:
#  - еженедельно записывает состояние портфеля(кол-во валюты, ее стоимость в $
#  - показывает какую долю от капитала каждая валюта занимает в портфеле

# Создаем словарь со списком недель и валютой, например 20,21 - недели

import json
from copy import deepcopy


# print(json.dumps(d, indent=2))  # indent-аргумент, который делает json-фаил подобный коду, добавляет отступы и
# переносы строк

def save_data(data):  # Сохраняем фаил
    with open("data1.json", "w") as f:
        json.dump(data, f, indent=2)


def load_data():  # Читаем сохраннный ранее фаил
    with open("data1.json") as f:
        data = json.load(f)
    return data


# СОЗДАЕМ ГРАФИК В ВИДЕ СТРОКИ СОСТОЯНИЯ ВАЛЮТ БЕЗ УЧЕТА НЕДЕЛЬ

def show_percent(name, percent, width=70):  # Функция принимает имя валюты, ее долю в портфеле и показывает
# пропрционально сколько доля занимает в портфеле
    fill = "█"  # заполненная шкала графика, символ скопировал с https://www.symbolsofit.com/
    empty = "-"  # пустая шкала графика
    bars = round(percent * width)

    progress = fill * bars + empty * (width - bars)  # создаем строку графика
    print(f"{name:8} - {round(percent * 100):2}% |{progress}|")  # задаем вид графика строки состояния


# СОЗДАЕМ ГРАФИК В ВИДЕ ГИСТОГРАММЫ

def plot_stat(data, signs, height=12):  # Функция делает два списка: 1-высоты столбцов, 2-подписи столбцов

    for i in range(height):
        if i % 3 == 0:
            current = max(data) - (max(data) - min(data)) / height * i
            line = f"{str(round(current, 2)):10}"
        else:
            line = " " * 10
        for num in data:
            if max(data) - (max(data) - min(data)) / height * (i + 1) < num:
                line += "█   "
            else:
                line += "    "

        print(line)

    print(f"{str(round(min(data), 2)):10}" + "█   " * len(data))
    print(" " * 10 + "█   " * len(data))
    line = (" " * 10)
    for sign in signs:
        line += f"{sign:4}"
    print(line)


# График изменения капитала

def show_convert(data):  # Функция переводит все валюты в доллары и показывает на графике сколько долларов в
# неделю переведено
    weeks = list(sorted(data.keys()))
    converted = []

    for week in weeks:
        currencies = data[week]
        total = 0
        for curr in currencies:
            total += curr["cost"] * curr["amount"]

        converted.append(round(total, 2))

        plot_stat(converted, weeks)


def show_stat(data, weeknum):  # Функция подсчитывает сколько каждая валта занимает в портфеле для какой-то недели и
    # показывает в виде прогресбаре от самой значимой к самой не значимой валюте
    total = 0
    for curr in data[weeknum]:
        total += curr["cost"] * curr["amount"]

    stats = []
    for curr in data[weeknum]:
        stats.append( (curr["cost"] * curr["amount"] / total, curr["name"]) )

    stats = reversed(sorted(stats))  # сортровка идет от меньшего к большему, разворачиваем список чтобы было от
# большего к меньшему

    for s, name in stats:
        show_percent(name, s)


# Создаем функцию для взаимодействия пользователя с приложением:

def select_mode():
    print()
    print("-" * 30)
    print("  Выберите режим работы:")
    print("  1. Добавьте новую неделю")
    print("  2. Скопировать новую неделю")
    print("  3. Добавьте информацию о валюте")
    print("  4. Измените информацию о валюте")
    print("  5. Вывести статистику")
    print("  6. Вывести распределение валют")
    print("  7. Выйти из программы")
    print("-" * 30)
    print()
    return int(input())


# Создаем бесконечный цикл для обработки команд

def loop():
    data = load_data()

    while True:

        mode = select_mode()

        if mode == 1:
            week = input("  Введите номер новой недели: ")
            data[week] = []
        elif mode == 2:
            week = input("  Введите номер новой недели: ")
            from_week = input("  Введите номер новой недели, откуда будем копировать: ")

            # source = []                               #Т.к. импортировали deepcopy, не актуально и можно заменить
            # for currency_dict in data[from_week]:
            #     source.append(currency_dict.copy())

            data[week] = deepcopy(data[from_week])
        elif mode == 3:
            week = input("  Введите номер недели: ")
            name = input("  Введите имя валюты: ")
            cost = float(input("  Введите стоимость валюты: "))
            amount = float(input("  Введите количество валюты: "))

            data[week].append({
                "name": name,
                "cost": cost,
                "amount": amount
            })
        elif mode == 4:
            week = input("  Введите номер недели: ")
            name = input("  Введите имя валюты: ")

            num = None
            for i, curr in enumerate(data[week]):
                if curr["name"] == name:
                    num = i

            if num == None:
                print("Нет такой валюты!")
            else:
                curr_cost = data[week][num]["cost"]
                cost = input(f"  Введите стоимость валюты ({curr_cost}): ")
                if cost:
                    data[week][num]["cost"] = float(cost)

                curr_amount = data[week][num]["amount"]
                amount = input(f"  Введите количество валюты ({curr_amount}): ")
                if amount:
                    data[week][num]["amount"] = float(amount)
        elif mode == 5:
            show_convert(data)
        elif mode == 6:
            week = input("  Введите номер недели: ")
            show_stat(data, week)
        elif mode == 7:
            break
        else:
            print("Некорректный режим")

    save_data(data)  # сохраняем на компьютер фаил


loop()
