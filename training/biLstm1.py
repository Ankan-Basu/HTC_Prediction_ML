import tensorflow as tf 
from tensorflow import keras
from tensorflow.keras.layers import Bidirectional, SimpleRNN, LSTM, Dense, TimeDistributed

model_bi_lstm = tf.keras.Sequential()

# Add the bidirectional LSTM layers
model_bi_lstm.add(Bidirectional(LSTM(50, return_sequences=True), input_shape=(120, 1)))
model_bi_lstm.add(Bidirectional(LSTM(100, return_sequences=True)))
model_bi_lstm.add(TimeDistributed(Dense(1)))