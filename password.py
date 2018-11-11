# 密码安全性检查代码
#
# 低级密码要求：
#   1. 密码由单纯的数字或字母组成
#   2. 密码长度小于等于8位
#
# 中级密码要求：
#   1. 密码必须由数字、字母或特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）任意两种组合
#   2. 密码长度不能低于8位
#
# 高级密码要求：
#   1. 密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合
#   2. 密码只能由字母开头
#   3. 密码长度不能低于16位
alp = r"abcdefghijklmnopqrstuvwxyz"
symbol = r"~!@#$%^&*()_=-/,.?<>;:[]{}\|"
number = r"123456789"
flag_len = 0
password = input("Please input your password:")
if(len(password) == 0 or password.isspace()):
    password = input("Your password is none , Please input again:")
if(len(password) <= 8):
    flag_len = 1
elif(16 > len(password) > 8):
    flag_len = 2
else:
    flag_len = 3
flag_con = 0
for each in password:
    if each in alp:
        flag_con += 1
        break
for each in password:
    if each in symbol:
        flag_con += 1
        break
for each in password:
    if each in number:
        flag_con += 1
        break
while 1:
    if(flag_len == 2 or flag_con == 2):
        print("Your password level is middle !")
    elif(flag_len == 1 or flag_con == 1):
        print("Your password level is low ！")
    else:
        print("Your password level is high !")
    break