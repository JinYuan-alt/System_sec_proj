import numpy
import numpy as np
import math

array=[1,2,3,4,5,6,7,8,9,]
x = numpy.array(array)
y = x.reshape(3,3)

def weights():
    pass

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

