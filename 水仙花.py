for i in range(100, 1000):
    百位 = int(i / 100)
    十位 = int((i - 100 * 百位) / 10)
    个位 = i % 10
    if i == 百位 ** 3 + 十位 ** 3 + 个位 ** 3:
        print(i)
