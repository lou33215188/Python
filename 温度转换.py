class Temp(float):
    def __new__(cls, a):
        real = a * 1.8 + 32
        return float.__new__(cls, real)


print(Temp(32))
