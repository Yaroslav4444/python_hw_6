"""
1) Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры времени,
оптимизировать, вновь выполнить замеры и ОПИСАТЬ СЛОВАМИ, что вы сделали и чего
 удалось добиться
"""
from timeit import timeit

print(timeit("""
list_of_numbers = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

sorted_list_of_numbers = [list_of_numbers[el] for el in
                          range(1, len(list_of_numbers))
                          if list_of_numbers[el] > list_of_numbers[el - 1]]

""", number=10000))

print(timeit("""
tuple_of_numbers = (300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55)

sorted_tuple_of_numbers = (list_of_numbers[el] for el in
                          range(1, len(list_of_numbers))
                          if list_of_numbers[el] > list_of_numbers[el - 1])

""", number=10000))

0.010518699884414673
0.005012999754399061

"""Заменил список на кортеж,получилось ускорить работу программы"""


print(timeit("""
def my_func(x, y):
    if y < 0:
        result = 1
        for i in range(y, 0):
            result *= x
        result = 1 / result
        return f"x = {x} в степени y = {y} будет = {result}"
""", number=1000000))

print(timeit("""
def my_func(x, y):
    print(pow(x, y))
""", number=1000000))

0.07145080016925931
0.0596238998696208

"""Сравнил скорость работы двух функций возведения числа в степень,первая с 
помощью цикла,вторая с помощью встроенной функции 'pow'.Время работы 
сократилось"""
