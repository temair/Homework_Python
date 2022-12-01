# №1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0.56 -> 11

# print("Введите вещественное число:")
# sum = 0
# str = input()
# for i in range(len(str)):
#     if str[i].isdigit():
#         sum += int(str[i])
# print("Сумма цифр числа = ", sum)

# №2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
#
# count = 1
#
# print("Введите  число N:")
# n = int(input())
# for i in range(1, n+1):
#     count = count * i
#     print(count, end=' ')

# №3 Задайте список из n чисел последовательности (1+1/n)*n выведите на экран их сумму.
# Пример: - - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
#
# print("Введите  число N:")
# n = int(input())
# summa = 0
#
# for i in range(1, n+1):
#     summa = summa + (1+1/i) ** i
# print(round(summa, 2))

# №4 Реализуйте алгоритм перемешивания списка

# import random
# #
# list = [1, 2, 3, 4, 5, 6, 7, 8]
# positoin = []
# mixed_list = []
#
# while len(list) != len(positoin):
#     j = random.randint(0, len(list)-1)
#     if not j in positoin:
#         positoin.append(j)
# print(list)
# print(positoin)
#
# for i in range(len(list)):
#     mixed_list.append(list[positoin[i]])
# print(mixed_list, end=' ')