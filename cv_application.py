# %%
import cv2 as cv
import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
from keras.preprocessing import image

# %%
cnn = tf.keras.models.load_model('cnn_model')


# %%
# %%
camObj = cv.VideoCapture(0)

# %%
while camObj.isOpened():
    ret, frame = camObj.read()
    frame = cv.resize(frame, (64, 64))

    # print(status)
    # print(frame.shape)

    # img = image.array_to_img(frame)

    # test_image = image.load_img(
    # 	img,
    # 	target_size=(64, 64)
    # )

    # test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(frame, axis=0)
    result = cnn.predict(x=test_image)

    if result[0][0] == 1:
        prediction = 'dog'
    else:
        prediction = 'cat'

    print(prediction)
