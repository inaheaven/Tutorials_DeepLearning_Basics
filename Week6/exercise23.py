import tensorflow_practice as tf
import numpy as np

data = np.loadtxt('./score2.csv', dtype=np.float32, delimiter=',')
print(data.shape)

table_row = data.shape[0]
table_col = data.shape[1]
print(table_row)
print(table_col)

y_column = 1
x_column = table_col - y_column

x_data = data[:, 0:(x_column)]
y_data = data[:, x_column:(x_column+1)]

print(x_data.shape)
print(y_data.shape)

x_test = [[20,40,50], [90,88,80]]
x=tf.placeholder(tf.float32, shape=[None, x_column])
y=tf.placeholder(tf.float32, shape=[None, y_column])

w = tf.Variable(tf.random_normal([x_column, y_column]))
b = tf.Variable(1.0)

H = tf.matmul(x,w)+b

diff = tf.square(H-y)
cost = tf.reduce_mean(diff)

learn_rate = 1e-5
optimizer = tf.train.GradientDescentOptimizer(learning_rate=learn_rate)
train = optimizer.minimize(cost)

sess= tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(50000):
    _t, _w, _c, _h = sess.run([train, w, cost, H], feed_dict={x:x_data, y:y_data})
    if step % 100 == 0:
        print('step: %d, loss: %f' % (step, _c))
        print('h', _h)

result = sess.run(H, feed_dict={x:x_test})
print('score preidct', result)