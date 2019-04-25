import numpy as np
import matplotlib.pyplot as plt

def myFunction(x):
    return 5.45 * x + 7.7

x = np.arange(26.0, 32.1, 2.0)
y = myFunction(x)

print(x)
print(y)

y_answer = [148, 164, 168, 183]
plt.plot(x, y_answer, marker ='o', color = 'b', linestyle = 'solid', label='label')

plt.plot(x, y_answer, marker ='o', color = 'r', linestyle = 'solid', label='prediction')

plt.xlim(x.min()-2, x.max()+2)
plt.ylim(y.min()-10, y.max()+10)
plt.grid(True)
plt.legend(loc='upper left')
plt.show()