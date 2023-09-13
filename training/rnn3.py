import tensorflow as tf 
from tensorflow import keras
from tensorflow.keras.layers import Bidirectional, SimpleRNN, LSTM, Dense, TimeDistributed

model_rnn = tf.keras.Sequential([
    SimpleRNN(50, return_sequences=True, input_shape=(120, 1)),
    SimpleRNN(100, return_sequences=True),
    SimpleRNN(100, return_sequences=True),
    SimpleRNN(100, return_sequences=True),
    TimeDistributed(Dense(1))
])