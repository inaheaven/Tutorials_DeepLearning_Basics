import tensorflow_practice as tf
x_data = [[73., 80., 75.], [93., 88., 93.], [89., 91., 90.], [96., 98., 100.], [73., 66., 70.]]
y_data = [[152.], [185.], [180.], [196.], [142.]]

x_test = [[20, 40, 50], [90, 88, 80]]

x_column = 3
y_column = 1
x = tf.placeholder(tf.float32, shape=[None, x_column])
y = tf.placeholder(tf.float32, shape=[None, y_column])

w = tf.Variable(tf.random_normal([x_column, y_column]))
b = tf.Variable(tf.random_normal([1]))

H = tf.matmul(x,w)+b
diff = tf.square(H-y)
cost = tf.reduce_mean(diff)

learn_rate = 1e-5
optimizer = tf.train.GradientDescentOptimizer(learning_rate=learn_rate)
train = optimizer.minimize(cost)

sess= tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(20001):
    _c, _h, _t = sess.run([cost, H, train], feed_dict={x:x_data, y:y_data})
    if step % 500 == 0:
        print('step:', step, "cost:", _c, "prediction", _h)
        print("====================")

result = sess.run(H, feed_dict={x: x_test})
print("score predict", result)