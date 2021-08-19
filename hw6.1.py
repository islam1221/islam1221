print('Hello,man!\n'
      "It's my game, where you write number 1-100 by yourself\n"
      "And my programm will searching its\n"
      "Let's play!\n")

import random
number = int(input('Put your number, for starting play with my programm:'))
count = 0
hot= number + 10
hot1 = number - 10
vhot = number + 5
vhot1 = number - 5
near = number + 25
near1 = number - 25
vnear = number + 90
vnear1 = number - 90
comp = random.randint(40,70)
comp1 = comp
while True:

    guess = comp1

    if guess <= vhot and guess >= vhot1:
        count +=1
        if guess <= number:
            print("so hot,bigger")
            comp1 += 1
        elif guess >= number:
            print("so hot, lower")
            comp1 -= 1

    elif guess <= hot and guess >= hot1:
        count +=1
        if guess <= number:
            print("hot,bigger")
            comp1 += 3
        elif guess >= number:
            print("hot,lower")
            comp1 -= 3

    elif guess <= near and guess >= near1:
        count += 1
        if guess <= number:
            print("near,bigger")
            comp1 += 25
        elif guess >= number:
            print("near,lower")
            comp1 -= 25
    elif guess <= vnear and guess >= vnear1:
        count += 1
        if guess <= number:
            print("near,bigger")
            comp1 += 40
        elif guess >= number:
            print("so near,lower")
            comp1 -= 40
    print(guess)
    if guess == number:
        print(f'Programm serching for {count} attempts')
        break
