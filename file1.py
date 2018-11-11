import pickle


def savefile(boy, girl):
    file_name_boy = 'boy_' + str(count) + '.txt'
    file_name_girl = 'girl_' + str(count) + '.txt'
    boy_file = open("D:\\test_txt\\" + file_name_boy, 'wb')
    girl_file = open("D:\\test_txt\\" + file_name_girl, 'wb')
    pickle.dump(boy, boy_file)
    pickle.dump(girl, girl_file)
    boy_file.close()
    girl_file.close()


f = open("D:\\hello.txt", 'r')
count = 1
boy = []
girl = []
for each_line in f:
    # 如果是分隔符，则判断保存为一个文件。
    if each_line[:2] != '==':
        (role, role_speak) = each_line.split(':', 1)
        if role == '王磊':
            boy.append(role_speak)
        else:
            girl.append(role_speak)
    else:
        savefile(boy, girl)
        count += 1
        boy = []
        girl = []
savefile(boy, girl)
f.close()
f = open("D:\\test_txt\\boy_1.txt", 'rb')
content_ = pickle.load(f)
print(str(content_))
