# from easygui import*


import random
secret = random.randint(1, 20)
print("---------------------====-----------------")
while True:
    try:
        temp = input("Please input my age :")
        guess = int(temp)
        break
    except ValueError as reason:
        print("Your input Value is error!")
        print("Try again!")
while guess != secret:
    if guess < secret:
        print("Your input is smaller than my age")
    else:
        print("You input is bigger than my age")
    print("Try again!")
    temp = input("Please input my age :")
    guess = int(temp)
print("Game over !\n")
