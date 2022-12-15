sp = [['00', '01', '02'], ['10','11', '12'], ['20', '21', '22']]
count = 1
play = 0
hod = True
print(*sp, sep = '\n')
print("Начнем игру! Перед тобой поле, номер позиции задается номером строки и номером столбца\n"\
      "Первая позиция это верхний левый угол или 00")
while hod == True and play < 9:
    play += 1
    row = int(input("Введите номер строки "))
    column = int(input("Введите номер столбца "))
    if count % 2:
        if (sp[row][column] != 'O') and (sp[row][column] != 'X'):
            sp[row][column] = 'X'
            print(*sp, sep = '\n')
            count += 1
            if (sp[0][0] == sp[0][1] == sp[0][2]) or (sp[1][0] == sp[1][1] == sp[1][2]) or\
                (sp[2][0] == sp[2][1] == sp[2][2]) or (sp[0][0] == sp[1][1] == sp[2][2]) or\
                (sp[0][2] == sp[1][1] == sp[2][0]) or (sp[0][0] == sp[1][0] == sp[2][0]) or\
                (sp[0][1] == sp[1][1] == sp[2][1]) or (sp[0][2] == sp[1][2] == sp[2][2]):
                print("Победил крестик!")
                hod = False
        else:
            print("Место занято, попробуйте другое ")
    else:
        if (sp[row][column] != 'O') and (sp[row][column] != 'X'):
            sp[row][column] = 'O'
            print(*sp, sep = '\n')
            count += 1
            if (sp[0][0] == sp[0][1] == sp[0][2]) or (sp[1][0] == sp[1][1] == sp[1][2]) or\
                (sp[2][0] == sp[2][1] == sp[2][2]) or (sp[0][0] == sp[1][1] == sp[2][2]) or\
                (sp[0][2] == sp[1][1] == sp[2][0]) or (sp[0][0] == sp[1][0] == sp[2][0]) or\
                (sp[0][1] == sp[1][1] == sp[2][1]) or (sp[0][2] == sp[1][2] == sp[2][2]):
                print("Победил нолик!")
                hod = False
        else:
            print("Место занято, попробуйте другое ")
if play == 9:
    print("Победила дружба :)")