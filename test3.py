count = 10


def mycount():
    global count
    count = 5


mycount()
print("%d" % count)
