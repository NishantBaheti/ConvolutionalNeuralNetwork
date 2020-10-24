from flask import Flask, Response, request
import json
from flask_cors import CORS
from mlModelUtility import MlUtility


app = Flask(__name__)
CORS(app)
modelPath = './cnn_model'


@app.route("/", methods=["GET"])
def home():
    respObj = {
        "status": "success",
        "message": "Up and Running Api"
    }
    response = Response(
        json.dumps(respObj),
        status=200,
        mimetype='application/json'
    )
    response.headers['Access-Control-Allow-Origin'] = '*'

    return response


@app.route("/getPredictionFromImageFile", methods=["GET", "POST"])
def getPredictionFromImageFile():
    if request.method == "POST":
        print(request.files)
        file = request.files['image']
        utilObj = MlUtility(modelPath=modelPath)
        img = utilObj.loadImageStream(fileObj=file)
        imageArray = utilObj.preprocessImage(imgObj=img)
        cnn_model = utilObj.loadModel()
        prediction = utilObj.generatePrediction(
            model=cnn_model, imageArray=imageArray)
        # print(prediction)
        respObj = {
            "status": "success",
            "message": "image received",
            "result": prediction
        }
        response = Response(json.dumps(respObj), status=200,
                            mimetype='application/json')
        response.headers['Access-Control-Allow-Origin'] = '*'

    else:
        respObj = {
            "status": "failure",
            "message": "method not found, only post allowed",
            "result": "undefined"
        }
        response = Response(json.dumps(respObj), status=404,
                            mimetype='application/json')
        response.headers['Access-Control-Allow-Origin'] = '*'

    return response


@app.route("/getPredictionFromImageString", methods=["GET", "POST"])
def getPredictionFromImageString():
    if request.method == "POST":
        # print(dir(request))
        imageObj = json.loads(request.data)

        imageString = imageObj['imageString'].split(',')[1]
        utilObj = MlUtility(modelPath=modelPath)
        img = utilObj.loadImageBase64(imageString=imageString)

        imageArray = utilObj.preprocessImage(imgObj=img)
        cnn_model = utilObj.loadModel()
        prediction = utilObj.generatePrediction(
            model=cnn_model, imageArray=imageArray)

        respObj = {
            "status": "success",
            "message": "image received",
            "result": prediction
        }
        response = Response(json.dumps(respObj), status=200,
                            mimetype='application/json')
        response.headers['Access-Control-Allow-Origin'] = '*'

    else:
        respObj = {
            "status": "failure",
            "message": "method not found, only post allowed",
            "result": "undefined"
        }
        response = Response(json.dumps(respObj), status=404,
                            mimetype='application/json')
        response.headers['Access-Control-Allow-Origin'] = '*'

    return response


# flask run -h 0.0.0.0 -p 5443 --cert=./cert/cvapp.crt --key=./cert/cvapp.key
