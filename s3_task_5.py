'''
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:

- для k = 8 список будет выглядеть так: 
[-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
'''

def fibonachi(number):
    num1, num2 = 1, 1
    num_list = [0]

    for i in range(number):
        num_list.append(num1)
        num_list.insert(0, num1*(-1)**i)
        num1, num2 = num2, num2 + num1
    print(num_list)

fibonachi(int(input("Введите число: ")))