x = 65
w = 2
b = 20
y = 165
H = w*x + b
cost = (H-y)**2
print('w=2,  b=20 몸무게 65, 키 165 비용함수')
print(y, H, cost)

x = [65, 80, 90, 45]
y = [165, 190, 160, 185]

def data(input):
    result = []
    for item in range(len(input)):
        result.append(2*input[item]+20)
    return result

H = data(x)

print(x)
print(H)
cost = 0
m = len(x)

for step in range(len(x)):
    cost += (H[step] - y[step]) ** 2
    print((H[step]-y[step]) **2, end = '')

cost = cost/m
print(cost)