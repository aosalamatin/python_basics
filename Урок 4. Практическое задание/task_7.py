"""
7. Реализовать генератор с помощью функции с ключевым словом yield,
 создающим очередное значение.

 При вызове функции должен создаваться объект-генератор.
 Функция должна вызываться следующим образом: for el in fact(n).
 Функция отвечает за получение факториала числа,
 а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.

Подсказка: факториал числа n — произведение чисел от 1 до n.
Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""

from itertools import count

def fact(x):
    result = 1
    i = 1
    while x >= i:
        result = result * i
        i += 1
        yield result


def fact_1(n):
    '''
    Функция отвечает за получение факториала числа
    :param number: число n факториал которого хотим получить
    :return: факториал числа n
    '''
    factorial = 1

    for x in count(1):
        if x > n:
            break

        factorial = factorial * x
        yield factorial



k = int(input("Число:"))

print("Работа моей функции:")
i = 1
for el in fact(k):
    print(f"{i}! = {el}")
    i += 1

print("Работа функции преподавателя:")
i = 1
for el in fact_1(k):
    print(f"{i}! = {el}")
    i += 1
