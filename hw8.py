family = [
    {
        'name': 'Mama',
        'phone': '0773545000',
    },
    {
        'name': 'Father',
        'phone': '0773335777'
    },
    {
        'name': 'Brother',
        'phone': '0770200811'
    },
    {
        'name': 'Sister',
        'phone': '0500333775'
    }
]
group_mates = [
    {
        'name': 'Esen',
        'phone': '0708601601'
    },
    {
        'name': 'Beka',
        'phone': '0507200427'
    },
    {
        'name': 'Adahan',
        'phone': '0707770999'
    }
]
list = []


def show_all_contact(lst):
    for i in lst[0]:
        print(*i.values())


def add_number(lst):
    show_all_contact(list)
    name = input('Enter name: ')
    phone = input('Enter phone: ')
    n = dict(name=name.title(), phone=phone)
    lst.append(n)
    show_all_contact(list)


def edit_name(lst):
    show_all_contact(list)
    name = input('Enter name for editing:')
    for i in lst:
        if i['name'] == name.title():
            name = input('Enter name:')
            i['name'] = name.title()
            show_all_contact(list)


def edit_number(lst):
    show_all_contact(list)
    contacts(list)
    name = input('Enter name for editing number: ')
    for i in lst:
        if i['phone'] == name.title():
            number = input('Enter number')
            i['phone'] = name.title()
            show_all_contact(list)


def delete_contact(lst):
    show_all_contact(list)
    name = input('Enter name for deleting: ')
    for i in lst:
        if i['name'] == name.title():
            contacts.remove(i)
    show_all_contact(list)


def searching_contact(lst):
    show_all_contact(list)
    name = input('Enter name for searching contacts:')
    for i in lst:
        if i['name'] == name.title():
            print(i['name'])
            print(i['phone'])


def choice_contact(lst):
    l = input("Your contacts|1-family|2-group mates|\n"
              "|")
    if l == "1":
        list.append(family)
    if l == "2":
        list.append(group_mates)
    show_all_contact(list)


def actions(lst):
    while True:
        command = input("Your actions:\n"
                        "0 - add contact\n"
                        "1 - edit name \n"
                        "2 - edit number\n"
                        "3 - delete\n"
                        "4 - searching\n"
                        "q - for quite\n"
                        "Your actions - ")
        if command == '0':
            add_number(list[0])
        elif command == '1':
            edit_name(list[0])
        elif command == '2':
            edit_number(list[0])
        elif command == '3':
            delete_contact(list[0])
        elif command == '4':
            searching_contact(list[0])
        elif command == 'q':
            print('program stop!')
            break


choice_contact(list)


actions(list)
