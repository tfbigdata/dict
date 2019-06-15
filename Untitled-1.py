import tensorflow as tf
from keras.datasets import mnist
from keras.backend.tensorflow_backend import set_session
import numpy as np

config = tf.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.45 
set_session(tf.Session(config=config))

f = np.load('./mnist.npz')
train_X, train_Y = f['x_train'], f['y_train']
test_X, test_Y = f['x_test'], f['y_test']
f.close()

from sklearn.preprocessing import OneHotEncoder
enc = OneHotEncoder()
train_Y_onehot = enc.fit_transform(train_Y.reshape(-1,1)).toarray()
test_Y_onehot = enc.fit_transform(test_Y.reshape(-1,1)).toarray()
train_X = train_X.reshape(*train_X.shape, 1)
test_X = test_X.reshape(*test_X.shape, 1)
print(train_X.shape, train_Y_onehot.shape)
print(test_X.shape, test_Y_onehot.shape)
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten,Conv2D, MaxPooling2D
from keras.layers import Activation
from keras.optimizers import Adam
input_shape=(28,28,1)

model = Sequential()
# block1
model.add(Conv2D(filters=32, kernel_size=(3, 3),
                activation='relu',
                input_shape=input_shape))
model.add(Conv2D(filters=64, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
# block2
model.add(Conv2D(filters=64, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.2))
# dense
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(10, activation='softmax'))
model.compile(loss='categorical_crossentropy',
              optimizer=Adam(lr=0.001),
              metrics=['accuracy'])
hist = model.fit(train_X, train_Y_onehot, epochs=30, batch_size=128)
score = model.evaluate(test_X, test_Y_onehot, batch_size=128)
print('accuracy=%s'%score[1])
