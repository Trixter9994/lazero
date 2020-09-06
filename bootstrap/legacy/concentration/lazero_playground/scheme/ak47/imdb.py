"""
Search for a good model for the
[IMDB](
https://keras.io/datasets/#imdb-movie-reviews-sentiment-classification) dataset.
"""
import numpy as np
import tensorflow as tf

# import autokeras as ak


def imdb_raw():
    max_features = 20000
    index_offset = 3  # word index offset
# better look into the shape.
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.imdb.load_data(
        num_words=max_features,
        index_from=index_offset)
    x_train = x_train
    y_train = y_train.reshape(-1, 1)
    x_test = x_test
    y_test = y_test.reshape(-1, 1)
    word_to_id = tf.keras.datasets.imdb.get_word_index()
    word_to_id = {k: (v + index_offset) for k, v in word_to_id.items()}
    word_to_id["<PAD>"] = 0
    word_to_id["<START>"] = 1
    word_to_id["<UNK>"] = 2
# unable to download dataset.
# all fucked up.
# check the directory.
# the deeplearning studio.
# too goddamn slow.
# dataset not included.
# must create own dataset.
    id_to_word = {value: key for key, value in word_to_id.items()}
    x_train = list(map(lambda sentence: ' '.join(
        id_to_word[i] for i in sentence), x_train))
    x_test = list(map(lambda sentence: ' '.join(
        id_to_word[i] for i in sentence), x_test))
    x_train = np.array(x_train, dtype=np.str)
    x_test = np.array(x_test, dtype=np.str)
    return (x_train, y_train), (x_test, y_test)
# why no fucking response?
# Prepare the data.
# this is fucked up.
# too damn slow.
(x_train, y_train), (x_test, y_test) = imdb_raw()
# make your dataset.
print(x_train)
# what the heck?
# must be smaller than 25000?
# print(x_train.shape)  # (25000,)
# print(y_train.shape)  # (25000, 1)
# print(x_train[0][:50])  # <START> this film was just brilliant casting <UNK>
# what are these things?
# # Initialize the TextClassifier
# clf = ak.TextClassifier(max_trials=3)
# # Search for the best model.
# clf.fit(x_train, y_train, epochs=2)
# # Evaluate on the testing data.
# what the fuck is going on?
# print('Accuracy: {accuracy}'.format(accuracy=clf.evaluate(x_test, y_test)))
