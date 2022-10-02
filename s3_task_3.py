'''
Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
между максимальным и минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''

from random import random
from copy import copy

def max_min_difference(number):
    num_list = []
    for i in range(number):
        num_list.append(round((random()*10), 2))
    print(num_list)
    new_list = copy(num_list)
    i=0
    while i < len(num_list):
        number1 = (new_list[i] * 10 //10) 
        number2 = num_list[i]
        num_list[i] = round((number2 - number1), 2)
        i+=1
    print(num_list)
    minimum = min(num_list)
    print(f"Минимальное число: {minimum}")
    maximum = max(num_list)
    print(f"Максимальное число: {maximum}")
    print(maximum - minimum)

    

num = int(input("Введите количество элементов: "))
max_min_difference(num)