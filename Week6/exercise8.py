import numpy as np
import matplotlib.pyplot as plt

def myfunction (w,x,b=7.7):
    return w*x + b

x = np.array([26,28,30,32])
y = np.array([148, 164, 168, 183])

b = 10
best = myfunction(5.45, x)
answer1 = myfunction( 3, x, b)
answer2 = myfunction( 6, x, b)
answer3 = myfunction( 9, x, b)

print(x)
print(y)
print(np.sum((best-y)**2))
print(np.sum((answer1-y)**2))
print(np.sum((answer2-y)**2))
print(np.sum((answer3-y)**2))

plt.plot(x,y, marker='o', color='y', linestyle='None', label='jumsu')
plt.plot(x, answer1, marker='o', color='r', linestyle='solid', label='answer1')
plt.plot(x, answer2, marker='o', color='g', linestyle='solid', label='answer2')
plt.plot(x, answer3, marker='o', color='b', linestyle='solid', label='answer3')

plt.legend(loc='upper right')
plt.xlim(25,35)
# plt.ylim(75,130)

plt.show()