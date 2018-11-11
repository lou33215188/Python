import ques

a = ques.result(1)
number = int(input("Please input a number : "))
i = 2
flag = 1
while i < number/2:
    if(number % i != 0):
        flag = 0
        break
    i = i + 15
if flag == 0:
    print("This number is not a prime !")
if flag == 1:
    print("This number is a prime")
