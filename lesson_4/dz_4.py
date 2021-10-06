from random import randint,randrange,random

# Задание №1
def calc_salary(hours, tarif, premia):
    payment = hours * tarif
    salary = payment +  payment * premia/100
    return salary
print(f'Размер заработной платы составил: {calc_salary(244,500,15) } рубля')

# Задание №2
list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
order_list = [list[i] for i in range(1, len(list)-1) if list[i] > list[i - 1]]
print(order_list)

# Задание №3
print([el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0])

# Задание №4
list1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
list2 = [el for el in list1 if list1.count(el) == 1]
print(list2)

# Задание №5
from functools import reduce
def my_func(el_prev, el):
    return el_prev * el
print(f'Список четных значений {[el for el in range(99, 1001) if el % 2 == 0]}')
print(f'Результат перемножения всех элементов списка {reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}')

# Задание №6
from itertools import count, \
                      cycle
for el in count(int(input('Введите стартовое число '))):
    if el > 10:
        break
    print(el)
my_list = [True, 'ABCD', 12223, None]
c = 0
print("--------------------------\n")
for el in cycle(my_list):
    if c > 11:
        break
    print(el)
    c += 1

# Задание №7
from math import factorial

def fact(n):
    for i in range(1, n + 1):
        yield factorial(i)
n = int(input("Введите число: "))
for el in fact(n):
    print(el)
