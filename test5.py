try:
    file_name = open("D:\\test_txt\\test1.txt",'w')
    file_name.write("i am existed!")
    sum = 1 + '1'
    file_name.close()
except TypeError as reason:
    print(str(reason))
finally:
    file_name.close()
