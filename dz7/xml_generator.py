import view

def create(abonent_first_name, abonent_name, abonent_tel):

    xml = '<xml>\n'
    xml += '   <first_name>{}</first_name>\n'\
    .format(abonent_first_name)
    xml += '   <name>{}</name>\n'\
        .format(abonent_name)
    xml += '   <tel>{}</tel>\n'\
        .format(abonent_tel)
    xml += '</xml>'

    with open('spravochnic.xml', 'w', encoding="utf-8") as page:
        page.write(xml)

    return xml