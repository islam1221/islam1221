#It's instruction for use this programm
print('hot - arround +-10\n'
      'super hot - arround +-5\n'
      'near - arround +-20\n'
      'so near - arround +-100\n')


import random
number = random.randint(1,100)
while True:
    try:
        tr = int(input("Put your attemps:"))
        c = tr
    except ValueError:
        print(f'Put only numbers')
        continue
# It's variable for future using this programm
    count = 0
    hot= number + 10
    hot1 = number - 10
    vhot = number + 5
    vhot1 = number - 5
    near = number + 25
    near1 = number - 25
    vnear = number + 100
    vnear1 = number - 100


    #While is cycle for repeat different movements
    while count != tr:
        try:
            guess = int(input("Put your're number 1-100:"))
        except ValueError:
            print(f'Put only numbers')
            continue

        if guess <= vhot and guess >= vhot1:
            count +=1
            if guess <= number:
                print("It's so hot,bigger")
            elif guess >= number:
                print("It's so hot, lower")

        elif guess <= hot and guess >= hot1:
            count +=1
            if guess <= number:
                print("It's hot,bigger")
            elif guess >= number:
                print("It's hot,lower")

        elif guess <= near and guess >= near1:
            count += 1
            if guess <= number:
                print("It's near,bigger")
            elif guess >= number:
                print("It's near,lower")

        elif guess <= vnear and guess >= vnear1:
            count += 1
            if guess <= number:
                print("It's so near,bigger")
            elif guess >= number:
                print("It's so near,lower")

        elif guess == 0:
            print('Программа завершена')
            break
        if guess == number:
            print(f'Вы угадали с {count} попыток\n'
                  '''░░░░░░░██████████████████░░░░░░░
    ░░░░████▓▓▓█▓▓▓▓▓▓▓▓█▓▓▓███░░░░░
    ░░░██▓▓█▓▓▓█▓▓▓▓▓▓▓▓█▓▓▓█▓▓█░░░░
    ░░██████████▓▓▓▓▓▓▓▓██████████░░
    ░░██──────███████████───────██░░
    ░███───────██▓▓▓▓▓▓█────────███░
    ░████───────█▓▓▓▓▓▓█───────████░
    ░█▓██───────█▓▓▓▓▓▓█───────██▓█░
    ░██▓█───────█▓▓▓▓▓▓█───────█▓██░
    ████▓█──────█▓▓▓▓▓▓█──────█▓████
    █▓██▓█──────▀██████▀──────█▓██▓█
    █▓██▓█────────────────────█▓██▓█
    █▓████────────────────────████▓█
    █▓██▀──────────────────────▀██▓█
    █▓██──█▀▀▀▀▄▄──────▄▄▀▀▀▀█──██▓█
    ███───█─────▀██▄▄██▀─────█───███
    ░██───▀█▄▄▄▄█▀────▀█▄▄▄▄█▀───██░
    ░███────────────────────────███░
    ░░█▓█──────────────────────█▓█░░
    ░░█▓▓█────────────────────█▓▓█░░
    ░░█▓▓▓█──────────────────█▓▓▓█░░
    ░░█▓▓▓█──────────────────█▓▓▓█░░
    ░░█▓▓▓▓█▄──────────────▄█▓▓▓▓█░░
    ░░░█▓▓█▀█──▄▀▀▀▀▀▀▀▀▄──█▀█▓▓█░░░
    ░░░░█▓█─▀▄▄▀────────▀▄▄▀─█▓█░░░░
    ░░░░░█▓█─────▄▄▄▄▄▄─────█▓█░░░░░
    ░░░░░░█▓█▄▄▄██▓▓▓▓██▄▄▄█▓█░░░░░░
    ░░░░░░░█▓▓▓█▓▓▓▓▓▓▓▓█▓▓▓█░░░░░░░
    ░░░░░░░░████████████████░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░''')
            break
        c1 -=1
        print(f"You have {c} attemps")

    if count == tr:
        print(f"You're loser\n"
              '''⊂_ヽ
    ＼＼ Λ＿Λ
    ＼( 'ㅅ' )
    >　⌒ヽ
    / 　 へ＼
    /　　/　＼＼
    ﾚ　ノ　　 ヽ_つ
    /　/
    /　/|
    (　(ヽ
    |　|、＼
    | 丿 ＼ ⌒)
    | |　　) /
    `ノ )　Lﾉ\n'''
              f"You number was {number}\n")

