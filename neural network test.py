import numpy
import numpy as np
import math

#A (when visualized pixels form to become a letter A and so on for the rest of data set.
a = [0, 0, 1, 1, 0, 0,
     0, 1, 0, 0, 1, 0,
     1, 1, 1, 1, 1, 1,
     1, 0, 0, 0, 0, 1,
     1, 0, 0, 0, 0, 1]
# B
b = [0, 1, 1, 1, 1, 0,
     0, 1, 0, 0, 1, 0,
     0, 1, 1, 1, 1, 0,
     0, 1, 0, 0, 1, 0,
     0, 1, 1, 1, 1, 0]
# C
c = [0, 1, 1, 1, 1, 0,
     0, 1, 0, 0, 0, 0,
     0, 1, 0, 0, 0, 0,
     0, 1, 0, 0, 0, 0,
     0, 1, 1, 1, 1, 0]

# Creating labels
y = [[1, 0, 0],
     [0, 1, 0],
     [0, 0, 1]]
# y = the prediction part.

def sigmoid(x):
    return 1 / (1 + np.exp(-x))
#activation function
def forward_prop():
    pass
#movement from input layer to output layer
def weights(x,y):
    l = []
    for i in range(x * y):
        l.append(np.random.randn())
    return (np.array(l).reshape(x, y))

def loss():
    pass

def backward_prop():
    pass
#meant to help with initializing weights, error handling.
def prediction():
    pass
def training():
    pass