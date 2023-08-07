import sys
sys.path.append('models/')
sys.path.append('preprocess/')
sys.path.append('training/')
sys.path.append('plotting/')
from preprocessing import *
# import the necessary model from ./training
from train import *

x_train, y_train = read_train_data()
x_valid, y_valid = read_valid_data()
x_test, y_test = read_test_data()

_, x_train, x_valid, x_test = scale_data(x_train, x_valid, x_test)

x_train = reshape_data(x_train)
x_valid = reshape_data(x_valid)
x_test = reshape_data(x_test)

y_train = reshape_data(y_train)
y_valid = reshape_data(y_valid)
y_test = reshape_data(y_test)

'''
Load pretrained model from ./models
or get model from ./training and train it
'''
model = None

'''If not pre-trained'''
train(model, epochs, x_train, y_train, x_valid, y_valid)

model.evaluate(x_train, y_train)
model.evaluate(x_valid, y_valid)
model.evaluate(x_test, y_test)