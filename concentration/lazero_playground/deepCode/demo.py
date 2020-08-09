import tensorflow as tf
import matplotlib.pyplot as plt

# %matplotlib inline
# jupyter
# remember there is nothing different from yesterday.
n = 500000
A = tf.truncated_normal((n,))
B = tf.random_uniform((n,)) # this is creepy.
# C=
a,b=None,None
with tf.Session() as sess:
    a, b = sess.run([A, B])
# And now
p0 = plt.hist(a, 100, (-4.2, 4.2))
# histogram?
plt.show(p0)
p1=plt.hist(b, 100, (-4.2, 4.2))
plt.show(p1)
# truncated ones are without tails