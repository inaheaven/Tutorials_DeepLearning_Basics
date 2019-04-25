import numpy as np
x = np.arange(1.0, 4.1, 0.5)

y = [3.1, 4.1, 4.9, 6.1, 6.9, 8.2, 9.1]

w = 0.132364
b = 0.111414

H = []
for step in range(len(x)):
    H.append(w*x[step]+b)

diff = []
for step in range(len(H)):
    diff.append((H[step]-y[step]) ** 2)

cost = 0.0
for step in range(len(diff)):
    cost += diff[step]
cost = cost/len(diff)

print(H)
print(diff)
print(cost)

