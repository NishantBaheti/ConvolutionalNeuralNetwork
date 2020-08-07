# %%
import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
from keras.preprocessing import image

# %%
cnn = tf.keras.models.load_model('cnn_model')


# %%
# pathToTestImage = '/home/nishant/Desktop/A-Z/original/DL Colab Changes/Convolutional_Neural_Networks 3/dataset/single_prediction/cat_or_dog_1.jpg'

pathToTestImage = '/home/nishant/Desktop/test.jpg'
test_image = image.load_img(
    path=pathToTestImage,
    target_size=(64, 64)
)
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis=0)
result = cnn.predict(x=test_image)

if result[0][0] == 1:
    prediction = 'dog'
else:
    prediction = 'cat'

print(prediction)
