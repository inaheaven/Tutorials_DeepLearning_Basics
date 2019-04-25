x = 1.0
y = 1.0
alpha = 0.01
m = 1
w = 5
H = w*x

print(w)
def calc(w):
    result = w -alpha * (1/m) * (w*x-y) *x
    return result

for step in range(2):
    w = calc(w)
    print('w', w)