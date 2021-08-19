print('Hello,man!\n'
      "It's instruction for using this programm\n"
      "If your number bigger write - b\n"
      "If your number smallest write - l\n"
      "If your number correct - y\n"
      "Let's play!\n")

min = 0
maks = 100
med = (min + maks)//2
count = 0

while 1:
    print(f"It's your number {med}?")
    ticket = input("l/b/y\n")
    if ticket == 'l':
        count += 1
        maks = med
        med = (min + maks)//2
    if ticket == 'b':
        count += 1
        min = med
        med = (min + maks)//2
    if ticket == "y":
        print(f'Programm WIN!on the {count} try')
        break
