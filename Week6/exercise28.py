import numpy as np
import matplotlib.pyplot as plt
import tensorflow_practice as tf

x_data = [2,4,6,8,10,12,14]
y_data = np.array([0,0,0,1,1,1,1])


w = tf.Variable(tf.random_normal([1], dtype=tf.float64, seed=0))
b = tf.Variable(tf.random_normal([1], dtype=tf.float64, seed=0))

H = 1/(1+np.e**(w * x_data+b))

cost = -tf.reduce_mean(y_data * tf.log(H)+(1-y_data)*tf.log(1-H))

learning_rate = 0.5

optimizer = tf.train.GradientDescentOptimizer(learning_rate)
train = optimizer.minimize(cost)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for i in range(60001):
        sess.run (train)
        if i % 6000 == 0:
            _cost, _w, _b = sess.run([cost, w, b])
            print('epoch:%.f, cost=%.4f, slope w = %.4f, bia b = %.4f' % (i, _cost, _w, _b))

