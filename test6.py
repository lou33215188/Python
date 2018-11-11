class A:
    def __init__(self):
        print("我从A进来了")
        print("我从A出去了")


class B(A):
    def __init__(self):
        print("我从B进来了")
        super(B, self).__init__()
        print("我从B出去了")


class C(A):
    def __init__(self):
        print("我从C进来了")
        super(C, self).__init__()
        print("我从C出去了")


class D(C, B):
    def __init__(self):
        print("我从D进来了")
        super(D, self).__init__()
        print("我从D出去了")


test = D()
print(D.mro())