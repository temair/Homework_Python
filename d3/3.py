# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# import random
#
# def generator_list(count_of_number, down_border, up_border):
#     list = []
#     for i in range(count_of_number):
#         list.append(random.randint(down_border, up_border))
#     return list
#
# list = generator_list(5,0,10)
# print(list)
# summa = 0
#
# for i in range(1, len(list)-1, 2):
#     summa += list[i]
#     i += 2
# print("Сумма элементов на нечетных позициях = ", summa)

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

# import random
#
# def generator_list(count_of_number, down_border, up_border):
#     list = []
#     for i in range(count_of_number):
#         list.append(random.randint(down_border, up_border))
#     return list
#
# list = generator_list(5,0,10)
# print(list)
# if len(list) % 2:
#     for i in range((len(list) // 2) + 1):
#         print(list[i] * list[-i - 1], end=' ')
# else:
#     for i in range(len(list) // 2):
#         print(list[i] * list[-i - 1], end=' ')

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19
#
# list = [1.1, 1.2, 3.1, 5, 10.01]
# list1 = []
# for i in range(len(list)):
#     list1.append(list[i] - int(list[i]))
# print(max(list1) - min(list1))

# Напишите программу, которая будет преобразовывать десятичное число в двоичное
# (встроенными методами пользоваться нельзя).
# Пример:
# 45 -> 101101

# print("Введите десятичное число для преобразования его в двоичное ")
# number = int(input())
# binar_number = ''
#
# while number // 2 != 0:
#     binar_number += str(number % 2)
#     number = number // 2
#
# binar_number += '1'
# print(binar_number[:: -1])
