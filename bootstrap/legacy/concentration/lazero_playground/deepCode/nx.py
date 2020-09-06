import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
v_1 = tf.constant([1, 2, 3, 4])
v_2 = tf.constant([2, 1, 5, 3])
v_add = tf.add(v_1, v_2)
with tf.Session() as sess:
  print(sess.run(v_add))