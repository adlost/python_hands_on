import random


def dice(num):
    if num == 1:
        print("----------")
        print("|        |")
        print("|    0   |")
        print("|        |")
        print("----------")
    elif num == 2:
        print("----------")
        print("|        |")
        print("| 0    0 |")
        print("|        |")
        print("----------")
    elif num == 3:
        print("----------")
        print("|    0   |")
        print("|    0   |")
        print("|    0   |")
        print("----------")

    elif num == 4:
        print("----------")
        print("| 0    0 |")
        print("|        |")
        print("| 0    0 |")
        print("----------")
    elif num == 5:
        print("----------")
        print("| 0    0 |")
        print("|    0   |")
        print("| 0    0 |")
        print("----------")
    else:
        print("----------")
        print("| 0    0 |")
        print("| 0    0 |")
        print("| 0    0 |")
        print("----------")


print("This is roll simulator")
while True:
    answer = int(input("Guess the number:  "))
    number = random.randint(1, 6)
    if answer == number:
        dice(number)
        print("Congratulation you win!!!")
    else:
        dice(number)
        print("You lose!!!")
