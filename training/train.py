import tensorflow as tf 
from tensorflow import keras

def train(model, epochs, x_train, y_train, x_valid, y_valid):
    model.compile(loss='mse', optimizer=keras.optimizers.Adam(learning_rate=0.001), metrics=[
        keras.metrics.RootMeanSquaredError(),
        keras.metrics.MeanAbsolutePercentageError()
    ])

    with tf.device('/device:GPU:0'):
        history = model_rnn.fit(x_train, y_train, epochs=epochs, validation_data=(x_valid, y_valid))

    return history