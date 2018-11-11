grade = int(input("Please input your grade:"))
if grade < 60:
    print("D")
else:
    if grade < 75:
        print("C")
    else:
        if grade < 85:
            print("B")
        else:
            print("A")
