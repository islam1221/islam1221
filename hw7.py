
import random
import datetime

number = random.randint(1, 100)
print("instruction:\n"
      "very hot +-5\n"
      "hot +-10\n"
      "cold +- 25"
      "very cold +-100")
count = int(input('put your attempts:'))
print("Let's go!\n"
      "Put your number:")

with open('text.txt1', 'a') as a:
    sec = datetime.datetime.now()
    while count != 0:
        try:
            guess = int(input(''))
        except ValueError:
            print("Put only numbers")
            continue

        if guess <= number + 5 and guess >= number - 5:
            count -= 1
            if guess < number:
                print("it's very hot, bigger")
            elif guess > number:
                print("it's very hot, lower")
        elif guess <= number + 10 and guess >= number - 10:
            count -= 1
            if guess < number:
                print("it's hot, bigger")
            elif guess > number:
                print("it's hot, lower")
        elif guess <= number + 25 and guess >= number - 25:
            count -= 1
            if guess < number:
                print("it's cold, bigger")
            elif guess > number:
                print("it's cold, lower")
        elif guess < (number + 25) and guess > 0 or guess > (number + 25) and guess <= 100:
            count -= 1
            if guess < number:
                print("it's very cold, bigger")
            elif guess > number:
                print("it's very cold, lower")
        else:
            print('Print namber into range')
        if guess == 0:
            print("Exit programm\n\n\n"
                "Made by Islamchik04")
            break
        if guess == number:
            print(f"You win from {count} time \nThanks for playing my game!\n")
            print(f"Guessed in {count} attempts!")
            sec1 = datetime.datetime.now() - sec
            a.write(f"You started in: {sec.strftime('%X')} \n")
            a.write(f"You finished in: {datetime.datetime.now().strftime('%X')} \n")
            a.write(f"You found number for {count} attempts\n")
            a.write(f"Time {sec1.seconds}\n")
            break
        if count == 0:
            print(f'End game;(\n'
                    f"Your number was {number}\n"
                  f"In future will be better:)")
            break         
      print(f"You have only {count}")
