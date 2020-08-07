# %%
import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
from keras.preprocessing import image
print(f"Tensorflow version {tf.__version__}")


# %%
# preprocessing of images

# image augmentations -- stop overlearn and overfit
# we are going to use these 3
# shear range
# zoom range
# horizontal flip
train_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)


training_set = train_datagen.flow_from_directory(
    '/opt/datasetsRepo/catDogDataset/training_set',
    target_size=(64, 64),
    batch_size=32,
    class_mode='binary')

# %%


# test dataset has to be kept intact for prod environment
test_datagen = ImageDataGenerator(rescale=1./255)

testing_set = test_datagen.flow_from_directory(
    '/opt/datasetsRepo/catDogDataset/test_set',
    target_size=(64, 64),
    batch_size=32,
    class_mode='binary')


# %%
# initializing Convolutional_Neural_Networks
cnn = tf.keras.models.Sequential()

# Convolution
cnn.add(tf.keras.layers.Conv2D(filters=32, kernel_size=3,
                               activation='relu', input_shape=[64, 64, 3]))
# Pooling
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))

# Adding Second Convolutional Layer
cnn.add(tf.keras.layers.Conv2D(filters=32, kernel_size=3, activation='relu'))
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))

# Flattening
cnn.add(tf.keras.layers.Flatten())

# Full Connection
cnn.add(tf.keras.layers.Dense(units=128, activation='relu'))

# Output Layer
cnn.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

# Compiling
cnn.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])


# %%
# training
cnn.fit(x=training_set, validation_data=testing_set,
        steps_per_epoch=2000, validation_steps=2000, epochs=10)


# %%
cnn.save('./cvPythonApi/cnn_model')

# %%
# Making Prediction

test_image = image.load_img(
    path='/opt/datasetsRepo/catDogDataset/single_prediction/cat_or_dog_1.jpg',
    target_size=(64, 64)
)
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis=0)
result = cnn.predict(x=test_image)


training_set.class_indices

if result[0][0] == 1:
    prediction = 'dog'
else:
    prediction = 'cat'


# %%
print(prediction)
