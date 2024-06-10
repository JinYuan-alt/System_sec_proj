import tensorflow

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
y = [0,1,2]
# y = the prediction part.

def sigmoid(x):
    pass
#activation function
def forward_prop():
    pass
#movement from input layer to output layer
def weights(x,y):
    pass
def loss():
    pass

def backward_prop():
    pass
#meant to help with initializing weights, error handling.
def prediction():
    pass
def training():
    pass