import csv

spravochnik = [["Иванов", "Иван", 89999999999],["Петров", "Петр", 89888888888],["Денисов", "Денис", 89777777777]]

def export_contact_cvs():
    with open("spravochnic_csv", mode="w", encoding="utf-8") as w_file:
        file_writer = csv.writer(w_file, delimiter=";", lineterminator="\r")
        for row in spravochnik:
            file_writer.writerow(row)

def export_contact_txt():
    with open('spravochnic_txt.txt', 'w', encoding="utf-8") as data:
        for i in spravochnik:
            for j in i:
                data.write(str(j))
                data.write('\n')
            data.write('\n')

def import_contact_from_txt():
    with open('spravochnic_txt.txt', 'r', encoding="utf-8") as data:
        for line in data:
            print(line)

def import_contact_from_cvs():
    export_csv_list = []
    with open("spravochnic_csv", encoding="utf-8") as r_file:
        reader_object = csv.reader(r_file, delimiter=';')
        for row in reader_object:
            export_csv_list.append(row)
            print(row)

def insert_abonent(abonent_first_name, abonent_name, abonent_tel):
    # spravochnik.insert(-1, [abonent_first_name, abonent_name, int(abonent_tel)])
    # print(spravochnik)
    with open("spravochnic_csv", mode="a", encoding="utf-8") as w_file:
        file_writer = csv.writer(w_file, delimiter=";", lineterminator="\r")
        file_writer.writerow([abonent_first_name, abonent_name, int(abonent_tel)])