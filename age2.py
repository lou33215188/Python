import random
import easygui as easy
secret = random.randint(1, 20)

title = "Guess My Age !"
msg = "What's is my age ? between 1 - 20"
guess = easy.integerbox(msg, title, lowerbound=1, upperbound=20)

while guess != secret:
    if guess > secret:
        easy.msgbox("You are bigeer than..")
    elif guess < secret:
        easy.msgbox("You are smaller than...")
    guess = easy.integerbox(msg, title, lowerbound=1, upperbound=20)

easy.msgbox("wow , you are right!")
