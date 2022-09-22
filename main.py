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

while True:
    print('''Доступні операції:
"+"-додавання;          "**"-зведення в ступінь;                          
"-"-віднімання;         "1/"-обернене число;
"*"-множення;           "log_e"-натуральний логорифм;   
"/"-ділення;            "log"-логорифм а по b;
"abs"-модуль числа;     "log_10"-десятичний логорифм;   
"a!"-факторіал;         "sqrt"-зведення до квадратного кореня;       
"cbrt"-зведення до кубічного кореня;
"off"-припинення програми.
''')

    choice_operation = input('Оберіть операцію: ')

    if choice_operation == 'off':
        break

    elif choice_operation in one_num:
        num1 = float(input('Введіть число: '))
        if choice_operation == '1/':
            opposite_number(num1)
        elif choice_operation == 'abs':
            absolute_number(num1)
        elif choice_operation == 'log_10':
            log_ten(num1)
        elif choice_operation == 'log_e':
            log_exp(num1)
        elif choice_operation == 'a!':
            factorial_(num1)
        elif choice_operation == 'sqrt':
            sqrt_(num1)
        elif choice_operation == 'cbrt':
            cuberoot(num1)

    elif choice_operation in two_nums:
        num1 = float(input('Введіть число 1: '))
        num2 = float(input('Введіть число 2: '))
        if choice_operation == '+':
            total_two_numbers(num1, num2)
        elif choice_operation == '-':
            subtraction_two_numbers(num1, num2)
        elif choice_operation == '*':
            product_two_numbers(num1, num2)
        elif choice_operation == '/':
            devision_two_numbers(num1, num2)
        elif choice_operation == '**':
            power_two_numbers(num1, num2)
        elif choice_operation == 'log':
            log_(num1, num2)

    else:
        print('\nIncorrect input\n')
