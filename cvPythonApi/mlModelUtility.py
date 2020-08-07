import tensorflow as tf
from keras.preprocessing import image
from PIL import Image
import cv2 as cv
import numpy as np
import base64
import io

class MlUtility:
    def __init__(self,modelPath):
        self.modelPath = modelPath

    def loadModel(self):
        model = tf.keras.models.load_model(self.modelPath)
        return model

    def loadImageStream(self,fileObj):
        # img = Image.read(fileObj.stream)
        img = image.load_img(
    		fileObj.stream,
    		target_size=(64, 64)
    	)
        return img

    def loadImageBase64(self,imageString):

        img = image.load_img(
            io.BytesIO(base64.b64decode(imageString)),
            target_size=(64,64)
        )
        return img


    def preprocessImage(self,imgObj):
        imageArray = image.img_to_array(imgObj)
        imageArray = np.expand_dims(imageArray, axis=0)
        return imageArray

    def generatePrediction(self,model,imageArray):
        result = model.predict(x=imageArray)
        print(result)
        if result[0][0] >= 0.5:
        	prediction = 'dog'
        else:
        	prediction = 'cat'

        return prediction