import tensorflow_practice as tf
x_data = [[10.0, 20, 30], [100, 90, 80], [50,55,45]]
y_data = [[40],[70],[50]]

x_test = [[20,40,50],[90,88,80]]

x_column = 3
y_column = 1

x = tf.placeholder(tf.float32, shape=[None, x_column])
y = tf.placeholder(tf.float32, shape=[None, y_column])
tf.placeholder(tf.int)
w = tf.Variable(tf.random_normal([x_column, y_column]))
b = tf.Variable(0.0)

H = tf.matmul(x,w) + b
diff = tf.square(H-y)
cost = tf.reduce_mean(diff)

learn_rate = 1e-5
optimizer = tf.train.GradientDescentOptimizer(learning_rate=learn_rate)
train = optimizer.minimize(cost)

sess= tf.Session()
sess.run(tf.global_variables_initializer())n

for step in range(10000):
    _t, _w, _c, _h = sess.run([train, w, cost, H], feed_dict={x: x_data, y:y_data})
    if step % 10 == 0:
        print("step:", step, "cost", _c, "prediction", _h)
        print("===============================")

result = sess.run(H, feed_dict={x:x_test})
print("prediction", result)