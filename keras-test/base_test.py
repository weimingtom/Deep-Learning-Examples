import numpy as np 
from keras.layers import MaxPooling2D
import keras.backend as K

val = np.array([[[[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]],
                 [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]],
                 [[-1,-1,-1],[-1,-1,-1],[-2,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]],
                 [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]],
                 [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]],
                 [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]],
                 [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]]])
print(val.shape) # (1, 6, 6, 3)
x = K.variable(value = val)
y = MaxPooling2D((3, 3), strides = 2, padding = 'same')(x)
#y = MaxPooling2D((3, 3), strides = 2, padding = 'valid')(x)
print(y.shape) # (1, 3, 3, 3)
print(y) # (1, 3, 3, 3)
print(K.eval(y))