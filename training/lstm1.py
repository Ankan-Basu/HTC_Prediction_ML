import tensorflow as tf 
from tensorflow import keras
from tensorflow.keras.layers import Bidirectional, SimpleRNN, LSTM, Dense, TimeDistributed

model_lstm = tf.keras.Sequential([
    LSTM(50, return_sequences=True, input_shape=(120, 1)),
    LSTM(100, return_sequences=True),
    TimeDistributed(Dense(1))
])