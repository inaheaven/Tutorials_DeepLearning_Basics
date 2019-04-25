import tensorflow_practice as tf

x = [26, 28, 30, 32]
y = [148, 164, 168, 183]

w = tf.Variable(tf.random_uniform([1], 0, 10, dtype = tf.float64, seed = 0))
b = tf.Variable(tf.random_uniform([1], 0, 10, dtype = tf.float64, seed = 0))

H = w * x + b
cost = tf.sqrt(tf.reduce_mean(tf.square(H-y)))

learning_rate = 1e-5

optimizer = tf.train.GradientDescentOptimizer(learning_rate)
train = optimizer.minimize(cost)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(20001):
        sess.run(train)
        if step % 100 == 0:
            print('Epoc: %f, cost funct = %.04f, slope w= %.4f, y b = %.4f' % (step,sess.run(cost), sess.run(w), sess.run(b)))