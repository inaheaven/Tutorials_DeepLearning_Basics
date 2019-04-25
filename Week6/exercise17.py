import tensorflow_practice as tf

x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

x_data = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
y_data = [3.1, 4.1, 4.9, 6.1, 6.9, 8.2, 9.1]

w = tf.Variable(1.0)
b = tf.Variable(1.0)

H = w * x + b

diff = tf.square(H-y)
cost = tf.reduce_mean(diff)

learn_rate = 1e-3
optimizer = tf.train.GradientDescentOptimizer(learning_rate=learn_rate)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())
for step in range(10000):
    _t, _w, _b, _c, _h = sess.run([train, w, b, cost, H], feed_dict={x: x_data, y: y_data})

    print('step:%d, cost: %f, weight: %f, bias: %f' % (step, _c, _w, _b))