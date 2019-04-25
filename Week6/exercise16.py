import tensorflow_practice as tf
sess= tf.Session()

a = tf.constant(1.0)
print(a, sess.run(a))

b = tf.constant(2.0, dtype=tf.float32)
print(b, sess.run(b))

c = a+b
print(c, sess.run(c))

d = tf.add(a,b)
print(d, sess.run(d))

e = tf.constant([1,2,3])
print(e, sess.run(e))

f = tf.constant([[1,2,3],[4,5,6]])
print(f, sess.run(f))