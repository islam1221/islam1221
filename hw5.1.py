
# Создайте массив состоящий из словарей с данными классов/аудиторий Гиктека

universities = [
    {
        'university' : 'AUCA',
        'chance' : False
    },
    {
      "university" : "Ala-Too",
        'chance' : False
    },
    {
        "university": "Manas",
        'chance' : False
    },
    {
        "university": "КРСУ",
        'chance' : False
    }
]
choice = []

# Напишите функцию которая принимает ранее созданный массив, фильтрирует
# полученный массив и возвращающает не менне двух элементов из массива
def check_chances(universities):
    for choices in universities:
        if choices['chance'] == False:
            print('Университет #', choices['university'], 'ждем заявку')
            choice.append(choices)
check_chances(universities)


# Напишите функцию которая принимает отфильтрованные данные, добавляет
# новое значение каждому из элементов отфильтрованных данных и возвращает
# измененные данные с добавленными значениями
def chances_third_univer(universities):
    for univer in universities:
        if univer['university'] == 'Ala-Too':
            univer['chance'] = True
            print("вы не приняты", univer)
chances_third_univer(choice)

# Напишите функцию которая принимает массив ранее измененых данных,
# меняет значение в каждом из элементов и возращает измененные данные
def leave_univer(univeresities):
    for univer in univeresities:
        if univer['chance'] == True:
            univer['chance'] = False
leave_univer(choice)

# Напишите функцию которая принимает массив ранее измененых данных,
# и поочередно выводит их в консоль
def show_in_console(universities):
    for univer in universities:
        print(univer)
show_in_console(choice)
