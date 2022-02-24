# Калькулятор Version 1.0
from random import randint


def action():
    """
Действия, которые можно использовать в калькуляторе :
"+" - сложение
"-" - вычитание
"*" - умножение
"/" - деление
"^" либо "**" - возведение в степень
"//" - частное
"%" - деление по модулю
"sqrt" либо "корень" - корень из числа (результат округляется)

Чтобы завершить работу калькулятора напишите "завершить", "стоп", "stop"
"""
    pass


d = True

print('Программа запущена')

try:
    while d:
        print('Если вам требуется помощь, введите help')
        What = (input('Выберите действие : '))

        if What == "help" or What == 'Help':
            print(action.__doc__)
            What = input('Выберите действие : ')

            if What == "Завершить" or What == "завершить" or What == "стоп" or What == "stop":
                break

        elif What == "Завершить" or What == "завершить" or What == "стоп" or What == "stop":
            break

        a = float(input('Введите первое число : '))
        b = float(input('Введите второе число : '))
        i = 0

        if What == "+" or What == "--":
            c = a + b
            print('Результат : ' + str(c))

        elif What == "-" or (What == "+-" or What == "-+"):
            c = a - b
            print('Результат : ' + str(c))
            print(' ')

        elif What == "*":
            c = a * b
            print('Результат : ' + str(c))
            print(' ')

        elif What == "/":
            c = a / b
            print('Результат : ' + str(c))
            print(' ')

        elif What == "//":
            c = a // b
            print('Результат : ' + str(c))
            print(' ')

        elif What == "%":
            c = a % b
            print('Результат : ' + str(c))
            print(' ')

        elif What == "^" or What == "**":
            c = a ** b
            print('Результат : ' + str(c))
            print(' ')

        elif What == "sqrt" or What == "корень":
            c = a ** (1 / b)
            print('Результат : ' + str(round(c)))
            print(' ')

        else:
            print('ЪУЪ СОБАКА, ЗАЧЕМ НАРУШАЕШЬ? БАН НАХРЕН!')
            d = False
            password = (randint(10000, 99999))
            print('Пароль для возобновления работы калькулятора : ' + str(password))
            f = int(input('Введите сюда полученный пароль : '))

            if f == password:
                print(' ')
                print('Работа программы возобновлена')
                d = True

            else:
                while i < 2:
                    i += 1
                    f = int(input('Неверный пароль. Введите пароль еще раз : '))
                    if f == password:
                        print(' ')
                        print('Работа программы возобновлена')
                        d = True
                        i = 2

                    elif i == 2:
                        print('Ты неисправим(а)... БАН!!!')
except ValueError:
    print('Допущена ошибка при вводе. Работа калькулятора завершена.')
