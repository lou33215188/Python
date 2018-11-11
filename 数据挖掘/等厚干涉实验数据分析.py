import numpy as np

Xleft = [24.970, 24.910, 24.760, 24.630, 24.462, 24.331, 24.137, 23.982, 23.801, 23.572]
Xright = [18.600, 18.667, 18.769, 18.912, 19.070, 19.239, 19.367, 19.550, 19.673, 19.910]
di = []
dx2 = []
sum_ = 0
result = 0
for index in range(len(Xleft)):
    di.append(Xleft[index]-Xright[index])

np.array(di)

print(di)
print(np.power(di, 2))
for index in range(5):
    dx2.append(np.power(di[index], 2) - np.power(di[index+5], 2))
print(dx2)
for each in dx2:
    sum_ = sum_ + each

print(sum_ / 5)
di_a = sum_/5

for each in range(0, 4):
    result += pow(dx2[each]-di_a, 2)
print(result)
th_re = np.sqrt(result/4)

print(th_re)
