import tensorflow_practice as tf
x1 = [2,4,6,8]
x2 = [0,4,2,3]
y = [81,93,91,97]

w1 = tf.Variable(tf.random_uniform([1], 0, 10, dtype=tf.float64, seed=0))
w2 = tf.Variable(tf.random_uniform([1], 0, 10, dtype=tf.float64, seed=0))
b = tf.Variable(tf.random_uniform([1], 0, 100, dtype=tf.float64, seed=0))

H = w1*x1 + w2*x2+b
cost = tf.sqrt(tf.reduce_mean(tf.square(H-y)))
learning_rate = 0.1

gradient_decent = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(2001):
        sess.run(gradient_decent)

        if step % 100 == 0:
            print('epoch %.f, cost = %.04f, weight1= %.4f, weight2 = %.4f y b = %.4f' % (step, sess.run(cost), sess.run(w1), sess.run(w2), sess.run(b)))