def file_compare(file1, file2):
    with open(file1) as f1, open(file2) as f2:
        count = 0  # 统计行数
        differ = []  # 统计不一样的数量
        for line1 in f1:
            line2 = f2.readline()
            count += 1
            if line1 != line2:
                differ.append(count)

    return differ


file1 = input("请输入需要比较的一个文件名:")
file2 = input("请输入另一个需要比较的文件名:")
differ = file_compare(file1, file2)

if len(differ) == 0:
    print("两个文件完全一样~！")
else:
    print("有%d处不同" % len(differ))
    for each_number in differ:
        print("第%d行不一样" % each_number)
