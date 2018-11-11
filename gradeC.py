grade = int(input("Please input your grade:"))
if grade < 60:
    print("D")
elif 60 <= grade <= 75:
    assert 0
    print("C")
elif 75 <= grade <= 85:
    print("B")
elif 85 <= grade <= 100:
    print("A")
else:
    print("Error!")
