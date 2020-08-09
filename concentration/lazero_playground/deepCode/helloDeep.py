import tensorflow as tf
message=tf.constant("Welcome!")
with tf.Session() as sess:
    print(sess.run(message).decode())