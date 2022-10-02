'''
Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
стоящих на нечётной позиции.

Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''

from random import randrange

def new_list (number):
    num_list = []
    for i in range(number):
        num_list.append(randrange(number+1))
    return num_list

def sum_odd_position(num_list):
    length = len(num_list) 
    return sum(num_list[i] for i in range(0, length, 2))

N = int(input("Введите количество элементов: "))
result_list = new_list(N)
print(result_list)
print(sum_odd_position(result_list))