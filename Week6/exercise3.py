import tensorflow_practice as tf
a = tf.constant(2)
b = tf.constant(1)
x = tf.Variable(5)

result = tf.add(tf.multiply(a,x),b)
sess = tf.Session()
sess.run(tf.global_variables_initializer())

print("a", a)
print(sess.run(a))
print(sess.run(result))