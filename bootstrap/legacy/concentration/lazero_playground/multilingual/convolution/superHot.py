import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import keras
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import confusion_matrix
from modelIO import saveTo
# what is useful anyway?
def niche(z):
    jerk=(lambda x:pd.read_csv(x))
    x0,y=jerk('canonical0.csv'),jerk('canonical1.csv')
    x=x0.iloc[:,:].values
    y0=y.iloc[:,z].values
#print(x)

    x0_train, x0_test, y0_train, y0_test = train_test_split(x, y0, test_size = 0.2)

    sc = StandardScaler()
    x0_train = sc.fit_transform(x0_train)
    x0_test = sc.transform(x0_test)

    classifier = Sequential()
    classifier.add(Dense(units = 6, kernel_initializer = 'uniform',activation = 'relu', input_dim = 10))
# i have counted this.
    classifier.add(Dense(units = 6, kernel_initializer = 'uniform',activation = 'relu'))
    classifier.add(Dense(units = 1, kernel_initializer = 'uniform',activation = 'sigmoid'))

# fuck you deeplearning!
    classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

    classifier.fit(x0_train, y0_train, batch_size = 10, epochs = 50)

    y0_pred = classifier.predict(x0_test)
    y0_pred = (y0_pred > 0.5)

    new_prediction = classifier.predict(sc.transform
    (np.array([[3,50.666666666666664,8.013876853447538,2,35.666666666666664,8.5,45,62,45,62]])))
    new_prediction = (new_prediction > 0.5)

    cm = confusion_matrix(y0_test, y0_pred)
    print (cm)
    saveTo(classifier,"conv"+str(z))
