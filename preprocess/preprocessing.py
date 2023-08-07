from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd

def read_train_data():
    x_train = pd.read_csv(f'{DATA_PATH}/temp_train.csv').to_numpy()
    y_train = pd.read_csv(f'{DATA_PATH}/htc_train.csv').to_numpy()
    return x_train, y_train

def read_valid_data():
    x_valid = pd.read_csv(f'{DATA_PATH}/temp_valid.csv').to_numpy()
    y_valid = pd.read_csv(f'{DATA_PATH}/htc_valid.csv').to_numpy()
    return x_valid, y_valid

def read_test_data():
    x_test = pd.read_csv(f'{DATA_PATH}/temp_test.csv').to_numpy()
    y_test = pd.read_csv(f'{DATA_PATH}/htc_test.csv').to_numpy()
    return x_test, y_test

# x_train_copy = x_train.copy()
# x_valid_copy = x_valid.copy()
# x_test_copy = x_test.copy()


def scale_data(x_train, x_valid, x_test):
    scaler = StandardScaler()
    scaler.fit(x_train)
    x_train = scaler.transform(x_train)
    x_valid = scaler.transform(x_valid)
    x_test = scaler.transform(x_test)
    return scaler, x_train, x_valid, x_test

# def reshape_data(x_train, x_valid, x_test):
#     x_train_seq = x_train.reshape(-1, 120, 1)
#     x_valid_seq = x_valid.reshape(-1, 120, 1)
#     x_test_seq = x_test.reshape(-1, 120, 1)

#     y_train_seq = y_train.reshape(-1, 120, 1)
#     y_valid_seq = y_valid.reshape(-1, 120, 1)
#     y_test_seq = y_test.reshape(-1, 120, 1)

def reshape_data(arr):
    '''
    Reshape data for fitting into RNNs, LSTMs
    '''
    return arr.reshape(-1, 120, 1)