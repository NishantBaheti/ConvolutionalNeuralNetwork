# %%
import cv2 as cv
import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
from keras.preprocessing import image
import time
# %%
cnn = tf.keras.models.load_model('model-v0.0.1')
classes = ['cats', 'dogs']

# %%
# %%
camObj = cv.VideoCapture(0)

# %%
while camObj.isOpened():
    ret, frame = camObj.read()
    cv.imshow('frame',frame)
    frame = cv.resize(frame, (128, 128))
    
    test_image = np.expand_dims(frame, axis=0)
    result = cnn.predict(x=test_image)

    print(dict(zip(classes,result[0])))
    time.sleep(2)
