def add_abonent():
    abonent_first_name = input("Введите Фамилию ")
    abonent_name = input("Введите Имя ")
    abonent_tel = input("Введите номер телефона ")
    return abonent_first_name, abonent_name, abonent_tel

# def view_contact():

def start():
    print("Выберте действие 1 - Экспорт контактов в формате csv, 2 - Экспорт контактов в формате txt")
    print("3 - Импорт контактов из файла txt, 4 - Импорт контактов из файла csv, 5 - добавить контакт")
    select = int(input())
    return select