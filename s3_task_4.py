'''
Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10
'''

def turn_into_number(num):
    result = []

    while num > 0:
        to_binary = num % 2
        result.insert(0, to_binary)
        num //= 2
    print(*result, sep = '')


number = int(input("Введите число: "))
turn_into_number(number)