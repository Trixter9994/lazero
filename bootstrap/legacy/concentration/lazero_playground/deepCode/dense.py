import tensorflow as tf
import os
import random
# finally:
#   pass
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
sess=tf.InteractiveSession()
t = tf.ones([2, 3, 4], tf.int32) # evaluate in backword direction.
# t0 = tf.zeros_like(t)
# t0 = tf.linspace(1.0, 2.0, 11)  # to be frank.
# t0 = tf.truncated_normal([2, 3], stddev=2, seed=12 * random.random())  # random data share statistical traits.
t0=tf.random_uniform([2,3],maxval=4,seed=12*random.random())
# weight close to 0
# T -> No dead neurons.
# what is wrong with the final digit?
print(t.eval())
print(t0.eval())
sess.close() # strange.