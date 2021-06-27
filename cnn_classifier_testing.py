# %%
import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
from keras.preprocessing import image

# %%
cnn = tf.keras.models.load_model('model-v0.0.1')
classes = ['cats','dogs']

# %%
pathToTestImage = './cat_test.jpg'
test_image = image.load_img(
    path=pathToTestImage,
    target_size=(128, 128)
)
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis=0)
result = cnn.predict(x=test_image)

print(dict(zip(classes,result[0])))
