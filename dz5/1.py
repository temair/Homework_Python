# 1 Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
#
# list_text = ['ПРИВЕТ', 'ЗАБВЕНИЕ', 'ПОКА']
# s = 'абв'
# #           Через  filter
# spisok = list(filter(lambda i: s not in i.lower(), list_text))
# #           Через списочное выражение
# list1 = [i for i in list_text if s not in i.lower()]
#
# print(spisok)
# print(list1)

# 2 Создайте программу для игры в ""Крестики-нолики"".
# sp = [['00', '01', '02'], ['10','11', '12'], ['20', '21', '22']]
# count = 1
# play = 0
# hod = True
# print(*sp, sep = '\n')
# print("Начнем игру! Перед тобой поле, номер позиции задается номером строки и номером столбца\n"\
#       "Первая позиция это верхний левый угол или 00")
#
# while hod == True and play < 9:
#     play += 1
#     row = int(input("Введите номер строки "))
#     column = int(input("Введите номер столбца "))
#     if count % 2:
#         sp[row][column] = 'X'
#         print(*sp, sep = '\n')
#         count += 1
#         if (sp[0][0] == sp[0][1] == sp[0][2]) or (sp[1][0] == sp[1][1] == sp[1][2]) or\
#             (sp[2][0] == sp[2][1] == sp[2][2]) or (sp[0][0] == sp[1][1] == sp[2][2]) or\
#             (sp[0][2] == sp[1][1] == sp[2][0]) or (sp[0][0] == sp[1][0] == sp[2][0]) or\
#             (sp[0][1] == sp[1][1] == sp[2][1]) or (sp[0][2] == sp[1][2] == sp[2][2]):
#             print("Победил крестик!")
#             hod = False
#     else:
#         sp[row][column] = 'O'
#         print(*sp, sep = '\n')
#         count += 1
#         if (sp[0][0] == sp[0][1] == sp[0][2]) or (sp[1][0] == sp[1][1] == sp[1][2]) or\
#             (sp[2][0] == sp[2][1] == sp[2][2]) or (sp[0][0] == sp[1][1] == sp[2][2]) or\
#             (sp[0][2] == sp[1][1] == sp[2][0]) or (sp[0][0] == sp[1][0] == sp[2][0]) or\
#             (sp[0][1] == sp[1][1] == sp[2][1]) or (sp[0][2] == sp[1][2] == sp[2][2]):
#             print("Победил нолик!")
#             hod = False
# print("Победила дружба :)")

# 3 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
#
# with open('file1.txt', 'w') as data:
#     data.write('')
#
# with open('file1.txt', 'w') as data:
#     data.write('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW')
#
# with open('file1.txt', 'r') as data:
#     line1 = data.readline()
#
# with open('file2.txt', 'w') as data:
#     data.write('')
#
# count1 = 1
#
# with open('file2.txt', 'a') as data:
#     for i in range(1, len(line1)):
#         if line1[i] == line1[i - 1]:
#             count1 += 1
#         else:
#             data.write(str(count1) + line1[i - 1])
#             count1 = 1
# with open('file2.txt', 'a') as data:
#     data.write(str(count1) + line1[- 1])
#
# with open("file2.txt", "r") as data:
#     line2 = data.readline()
#
# with open('file.txt', 'w') as data:
#     data.write('')
#
# count_num = ''
# with open('file.txt', 'a') as data:
#     for i in range(len(line2)):
#         if line2[i].isdigit():
#             count_num += line2[i]
#         else:
#             for j in range(int(count_num)):
#                 data.write(line2[i])
#             count_num = ''
#