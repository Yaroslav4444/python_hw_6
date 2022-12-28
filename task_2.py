"""Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры памяти,
оптимизировать, вновь выполнить замеры и подготовить аналитику, что вы сделали
и чего удалось добиться"""

from functools import reduce
from random import randrange
from memory_profiler import profile


@profile
def memory_measurements_1():
    """Формирование списка через цикл"""
    lst_new = []
    for i in range(1, len(lst)):
        if lst[i] > lst[i - 1]:
            lst_new.append(lst[i])
    print(lst_new)


@profile
def memory_measurements_2():
    """Формирование списка через LC"""
    list_new_2 = [lst[el] for el in range(1, len(lst)) if
                  lst[el] > lst[el - 1]]
    print(list_new_2)


"""Оптимизация формирования списка не дала ожидаемого результата :("""


@profile
def memory_measurements_4():
    """Функция формирования стандартного списка и умножения через цикл"""
    list_multi = [el for el in range(100, 1001) if el % 2 == 0]
    multiplication = 1
    for el in list_multi:
        multiplication *= el
    print(multiplication)


@profile
def memory_measurements_3():
    """Функция формирования списка с использованием лямбда функции и генератора
        списка"""
    print(reduce((lambda x, y: x * y),
                 (el for el in range(100, 1001) if el % 2 == 0)))

    """Сравниваем две функции формирования списка четных чисел в диапазоне от
    100 до 1000 и их произведения с применение лямбда и цикла for. Оптимизация 
    не дала ожидаемого результата :("""


n = 100
lst = [randrange(100) for el in range(n)]
print(lst)
memory_measurements_1()
memory_measurements_2()
memory_measurements_3()
memory_measurements_4()
