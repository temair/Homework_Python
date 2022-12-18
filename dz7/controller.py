import view
import model
import xml_generator


def main_function():
    select = view.start()
    if select == 1:
        model.export_contact_cvs()

    elif select == 2:
       model.export_contact_txt()

    elif select == 3:
       model.import_contact_from_txt()

    elif select == 4:
        model.import_contact_from_cvs()

    elif select == 5:
        abonent_first_name, abonent_name, abonent_tel = view.add_abonent()
        model.insert_abonent(abonent_first_name, abonent_name, abonent_tel)
        answer = input("Хотите добавить запись в xml файл? Если да, нажмите 1 ")
        if answer == '1':
            xml_generator.create(abonent_first_name, abonent_name, abonent_tel)