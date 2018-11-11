import copy
a = [1, [1, 2, 3], [4, 5, 6]]
b = a
c = copy.copy(a)
d = copy.deepcopy(a)
a.append(15)
a[1][2] = 10
a[0] = 0
print(a)
print(b)
print(c)
print(d)
print(id(a))
print(id(b))
print(id(c))
print(id(d))
