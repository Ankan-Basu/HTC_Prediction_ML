import tensorflow as tf 
from tensorflow import keras
from tensorflow.keras.layers import Dense

model__ff1 = keras.models.Sequential([
    (keras.layers.Input(shape=x_train.shape[1:])),
    (keras.layers.Dense(50, activation='relu')),
    (keras.layers.Dense(120))
])