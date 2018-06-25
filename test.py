import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
print(tf.__version__)
hello = tf.constant('hello world',dtype='string')
session = tf.Session()
print(session.run(hello))
a = tf.constant(11)
b = tf.constant(39)
print(session.run(a+ b))
print('hellow')

