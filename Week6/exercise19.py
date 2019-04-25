import tensorflow_practice as tf

x_data = [[73., 80., 75.], [93., 88., 93.], [89., 91., 90.], [96., 98., 100.], [73., 66., 70.]]
y_data = [[152.], [185.], [180.], [196.], [142]]

x_column = 3
y_column = 1

x = tf.placeholder(tf.float32, shape=[None, x_column])
y = tf.placeholder(tf.float32, shape=[None, x_column])

w= tf.Variable(tf.random_normal([x_column, y_column]), name='weight')
b= tf.Variable(tf.random_normal([1]), name='bias')

hypothesis = tf.matmul(x,w) +b
