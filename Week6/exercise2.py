import tensorflow_practice as tf

a = tf.constant(14)
b = tf.constant(5)

add = a+b
sub = a-b
mul = a*b
div = a/b

sess = tf.Session()

print(sess.run(add))
print(sess.run(sub))
print(sess.run(mul))
print(sess.run(div))