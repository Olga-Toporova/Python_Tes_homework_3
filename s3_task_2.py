'''
Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый 
и последний элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
'''

from random import randrange


def new_list(number):
    num_list = []
    for i in range(number):
        num_list.append(randrange(11))
    return num_list


def result_sum(origin_list):
    result = []
    length = len(origin_list)
    for i in range(length // 2):
        result.append(origin_list[i] * origin_list[length - 1 - i])
    if length % 2 != 0:
        result.append(origin_list[length // 2 ])
    print(result)


n = int(input("Введите количество элементов: "))
result_list = new_list(n)
print(result_list)
result_sum(result_list)