import tensorflow_practice as tf
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1.0, 4.1, 0.5)
y = [3.1, 4.1, 4.9, 6.1, 6.9, 8.2, 9.1]

w= tf.Variable(0.1)
b = tf.Variable(0.1)

H = w * x + b

diff = tf.square(H-y)
cost = tf.reduce_mean(diff)

learn_rate = 1e-3
optimizer = tf.train.GradientDescentOptimizer(learning_rate= learn_rate)
train = optimizer.minimize(cost)

sess = tf.Session()

sess.run(tf.global_variables_initializer())

cost_list = []
weight_list = []

for step in range(10000):
    sess.run(train)
    cost_list.append(sess.run(cost))
    weight_list.append(sess.run(w))
    print('step: %d, cost: %.12f, weight: %f, bias:%f' % (step, sess.run(cost), sess.run(w), sess.run(b)))

plt.title('cost func')
plt.plot(cost_list, 'b')
plt.xlabel('step')
plt.ylabel('cost val')
plt.grid(True)
plt.show()


plt.title('cost val')
plt.plot(weight_list, 'r')
plt.xlabel('step')
plt.ylabel('weight val')
plt.grid(True)
plt.show()