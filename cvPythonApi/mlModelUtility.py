import tensorflow as tf
from keras.preprocessing import image
from PIL import Image
import cv2 as cv
import numpy as np

class MlUtility:
    def __init__(self,modelPath):
        self.modelPath = modelPath

    def loadModel(self):
        model = tf.keras.models.load_model(self.modelPath)
        return model

    def loadImage(self,fileObj):
        # img = Image.read(fileObj.stream)
        img = image.load_img(
    		fileObj.stream,
    		target_size=(64, 64)
    	)
        return img

    def preprocessImage(self,imgObj):
        imageArray = image.img_to_array(imgObj)
        imageArray = np.expand_dims(imageArray, axis=0)
        return imageArray

    def generatePrediction(self,model,imageArray):
        result = model.predict(x=imageArray)
        if result[0][0] == 1:
        	prediction = 'dog'
        else:
        	prediction = 'cat'
        print(result[0])

        return prediction
