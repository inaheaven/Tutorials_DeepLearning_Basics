import numpy as np

x = [26, 28, 30, 32]
y = [148, 164, 168, 183]

mx = np.mean(x)
my = np.mean(y)

print(mx)
print(my)

bunmo = sum([(mx-i)**2 for i in x])

def top(x, mx, y, my):
    d = 0
    for i in range(len(x)):
        d +=(x[i]-mx) * (y[i]-my)
    return d

bunja = top(x, mx, y, my)

print(bunmo)
print(bunja)

a = bunja/bunmo
b = my - (mx*a)

print('slope', a)
print('y', b)