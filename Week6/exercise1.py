import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow_practice as tf

# 상수정의
a = tf.constant(120, name='a')
b = tf.constant(130, name='b')

# 변수 정의 및 초기 값 할당하기
v = tf.Variable(0, name='v')

print(a)
print(b)
print(v)
result = a+b
print(result)

sess = tf.Session()
print('결과:', sess.run(result))
aa, bb, cc = sess.run([a,b,result])
print(aa)
print(bb)
print(cc)