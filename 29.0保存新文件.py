file_name = input("请输入文件名:")
my_file = file_name + '.txt'
file_write = open("D:\\test_txt\\" + my_file, 'w')
print("请输入内容(单独输入'w'保存退出)")
while True:
    file_write_something = input()
    if file_write_something != 'w':
        file_write.write(file_write_something + '\n')
    else:
        break
file_write.close()
