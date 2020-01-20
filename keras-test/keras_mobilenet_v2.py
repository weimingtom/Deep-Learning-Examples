from keras.preprocessing.image import load_img 
from keras.preprocessing.image import img_to_array
from keras.applications.mobilenet_v2 import preprocess_input
from keras.applications.mobilenet_v2 import decode_predictions
from keras.applications.mobilenet_v2 import MobileNetV2

import tensorflow as tf 
config = tf.ConfigProto(gpu_options=tf.GPUOptions(allow_growth=True))
sess = tf.Session(config=config)

# load the model
model = MobileNetV2(weights='/media/wx/diskE/weights/keras/mobilenet_v2_weights_tf_dim_ordering_tf_kernels_1.4_224.h5', alpha=1.4)
model.summary()
# load an image from file
image = load_img('./data/bike.jpg', target_size=(224, 224))
# convert the image pixels to a numpy array
image = img_to_array(image)
# reshape data for the model
image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
# prepare the image for the VGG model
image = preprocess_input(image)
# predict the probability across all output classes
yhat = model.predict(image)
print(yhat.shape)
# convert the probabilities to class labels
label = decode_predictions(yhat)
print(label)
# retrieve the most likely result, e.g. highest probability
label = label[0][0]
print(label)
# print the classification
print('%s (%.2f%%)' % (label[1], label[2]*100))
