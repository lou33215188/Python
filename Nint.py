class Nint(int):
    def __new__(cls, asc):
        total = 0
        if isinstance(asc, str):
            for each in asc:
                total += ord(each)
            asc = total
        return int.__new__(cls, asc)


print(Nint('i'))
