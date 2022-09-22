from math import *


def total_two_numbers(a, b):
    return print(f'\nРезультат: {a + b}\n')


def subtraction_two_numbers(a, b):
    return print(f'\nРезультат: {a - b}\n')


def product_two_numbers(a, b):
    return print(f'\nРезультат: {a * b}\n')


def devision_two_numbers(a, b):
    if b != 0:
        return print(f'\nРезультат: {a / b}\n')
    else:
        return print('\nIncorrect divisior\n')


def power_two_numbers(a, b):
    if a != 0:
        return print(f'\nРезультат: {a ** b}\n')
    else:
        return print('\nIncorrect input\n')


def log_(a, b):
    return print(f'\nРезультат: {log(a, b)}\n')


def opposite_number(a):
    if a != 0:
        return print(f'\nРезультат: {1 / a}\n')
    else:
        return print('\nIncorrect number\n')


def absolute_number(a):
    return print(f'\nРезультат: {abs(a)}\n')


def log_ten(a):
    return print(f'\nРезультат: {log(a, 10)}\n')


def log_exp(a):
    return print(f'\nРезультат: {log(a)}\n')


def factorial_(a):
    return print(f'\nРезультат: {factorial(a)}\n')


def sqrt_(a):
    return print(f'\nРезультат: {a ** 0.5}\n')


def cuberoot(a):
    return print(f'\nРезультат: {a ** (1 / 3)}\n')


one_num = '1/', 'abs', 'log_10', 'log_e', 'a!', 'sqrt', 'cbrt'
two_nums = '+', '-', '*', '/', '**', 'log'
