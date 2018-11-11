class Target:
    count = 0

    def __init__(self):
        Target.count += 1

    def __del__(self):
        Target.count -= 1


a = Target()
b = Target()
print(Target.count)
del a
print(Target.count)
