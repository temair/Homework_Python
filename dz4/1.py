# №1 Округлить число Пи по заданной точности

# Метод округления чисел
# def my_raunding(number, number_raund):
#     dr = number.split(".")
#     str1 = dr[1]
#     str2 = ''
#     i = 0
#
#     if len(dr[1]) == number_raund:
#         print("Ваше число уже округлено до нужного знака!")
#         exit()
#
#     while i < number_raund:
#         str2 = str2 + str1[i]  # В переменную str2 собираем дробную часть числа
#         i += 1
#
#     if int(str1[number_raund]) >= 5:  # Проверяем следующую цифру числа после необходимой позиции округления
#         a = int(str2[i - 1]) + 1  # Если >= 5, то преобразуем строку в список, чтобы вставить цифру больше на 1
#         b = list(str2)
#         b.insert(i - 1, str(a))
#         b.pop()  # Обрезаем до нужной позиции округления
#         print(dr[0] + "." + "".join(b))
#     else:
#         print(dr[0] + "." + str2)
#
#
# number = input("Введите число, которое вы хотите округлить, целую часть от дробной отделите точкой! ")
# number_raund = int(input("Введите сколько знаков после точки нужно оставить "))
# my_raunding(number, number_raund)
#
# from math import pi
#
# print(pi)
# my_raunding(str(pi), number_raund=4)

# №2 Разложение числа на простые множители col = [2,3,5,7,11,13]

# n = int(input("Введите число "))
# simple_multipliers = []
#
# while n >= 2:
#     if not n % 2:
#         simple_multipliers.append(2)
#         n /= 2
#     elif not n % 3:
#         simple_multipliers.append(3)
#         n /= 3
#     elif not n % 5:
#         simple_multipliers.append(5)
#         n /= 5
#     elif not n % 7:
#         simple_multipliers.append(7)
#         n /= 7
#
# print(simple_multipliers, end=' ')

# №3 Из списка выбрать элементы, встречающиеся в нем единожды

# colection = [1, 2, 1, 3, 2, 4, 5]
# count1 = 0
# colection_one_element = []
# for i in colection:
#     count1 = colection.count(i)
#     if count1 == 1:
#         colection_one_element.append(i)
# print(colection_one_element, end=' ')

# №4 Записать в файл многочлен заданной степени с рандомными коэффициентами

import random

k = int(input("Введите степень многочлена "))
exponent_list = []
coefficient_list = []

for i in range(k, 0, -1):
    exponent_list.append(i)

for i in range(k):
    coefficient_list.append(random.randint(0, 100))

with open('file.txt', 'w') as data:
    data.write('')

with open('file.txt', 'w') as data:
    for i in range(k):
        data.write(str(coefficient_list[i])+'x'+'^'+str(exponent_list[i])+'+')
    data.write(str(random.randint(0, 100))+' = 0')