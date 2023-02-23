# Задание
# Создать приложение которое анализирует анкеты посетителей, должно отражаться:
#  - среднее время ожидания клиента в очереди
#  - загруженность МФЦ с предложением оптимального времени посещения
#  - эффективность работы отделения, выраженное в количестве услуг, оказанных за выбранный период времени


import json
import datetime

open_time = 10
close_time = 21


def check_date(str_date):
    if len(str_date.split("-")) != 3:
        return False
    year, month, day = str_date.split("-")
    if len(year) != 4 or len(month) != 2 or len(day) != 2:
        return False
    if not (year.isdigit() and month.isdigit() and day.isdigit()):  # isdigit - проверяет что данные являются числом
        return False
    year, month, day = int(year), int(month), int(day)
    if 1000 <= year <= 3000 and 1 <= month <= 12 and 1 <= day <= 31:
        return True
    else:
        return False


def ask_date():
    print("Введите дату: ")
    date = None
    while date is None:
        temp = input()
        if check_date(temp):
            date = temp
        else:
            print("Введена некорректная дата")
    return date


def list_stat(A):
    counter = {}
    for time in range(open_time, close_time + 1):
        counter[time] = 0

    for number in A:
        counter[number] += 1

    return counter


def list_sort(A):
    counter = list_stat(A)
    items = list(counter.items())
    items.sort(key=lambda x: x[1])
    return items


def load_info():
    with open("info.json") as f:
        info = json.load(f)
    return info


def compare_dates(date_1, date_2, date_3):
    date_1 = datetime.date.fromisoformat(date_1)
    date_2 = datetime.date.fromisoformat(date_2)
    date_3 = datetime.date.fromisoformat(date_3)
    return date_1 <= date_2 <= date_3


def calc_mean_wait(stat):
    s = 0
    cnt = 0
    for record in stat:
        s += record["wait"]
        cnt += 1
    mean = s / cnt
    print(f"Среднее время ожидания: {mean}")


def calc_optimization(stat):
    A = []
    for record in stat:
        A.append(record["hour"])

    hours = list_sort(A)

    print("Часы работы от наименьшей загруженности до наибольшей: ")
    for hour, workload in hours:
        print(f"{hour}:00 - {workload} человек")


def calc_productivity(stat, date_begin, date_end):
    count = 0

    for record in stat:
        if compare_dates(date_begin, record["date"], date_end):
            count += 1
    print(f"Оказано услуг за выбранный период: {count}")


def main():
    stat = load_info()
    calc_mean_wait(stat)
    calc_optimization(stat)
    print("Введите начало временного периода: ")
    date_begin = ask_date()
    print("Введите конец временного периода: ")
    date_end = ask_date()

    calc_productivity(stat, date_begin, date_end)


main()
