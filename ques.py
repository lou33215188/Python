def result(i):
    return i*(i+2)*(i+4)*(i+6)*(i+8)*(i+10)


i = 1
while True:
    k = 2 * i - 1           # k = 2i-1  则k为奇数
    if result(k) == 135135:
        break
    else:
        i += 1

print('这几个数是%d %d %d %d %d %d' % (k, k+2, k+4, k+6, k+8, k+10))
