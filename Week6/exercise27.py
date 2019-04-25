import matplotlib.pyplot as plt
import numpy as np


def sigmoid(weight, x):
    return 1 / (1+np.exp(-weight*x))

x = np.arange(-5.0, 5.0, 0.1)
y1 = sigmoid(1,x)
y2 = sigmoid(2,x)


plt.plot(x, y1, color='r', label='weight=1')
plt.plot(x, y2, color='b', label='weight=2')

plt.ylim(-0.1, 1,1)
plt.legend(loc='upper left')
plt.show()