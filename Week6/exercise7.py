import numpy as np
import matplotlib.pyplot as plt

def myfunction(x):
    return 6*x + 10

x = np.array([26,28, 30,32])
y = np.array([148, 164, 168, 183])

answer = myfunction(x)
print(x)
print(y)
print(answer)

print('오차 제곱의 합:', np.sum((answer-y)**2))

plt.plot(x,y, marker='o', color='g', linestyle='None', label='jumsu')
plt.plot(x,answer, marker='o', color='r', linestyle='solid', label='prediction')

for idx in range(len(x)):
    xdata = []
    ydata = []
    xdata.append(x[idx])
    ydata.append(y[idx])

    xdata.append(x[idx])
    ydata.append(answer[idx])

    plt.plot(xdata, ydata, marker='', color='b', linestyle='solid')

plt.legend(loc='upper left')
plt.show()