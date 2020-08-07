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
    response = Response(json.dumps(respObj), status=200,
                        mimetype='application/json')
    response.headers['Access-Control-Allow-Origin'] = '*'

    return response


@app.route("/getPrediction", methods=["GET", "POST"])
def getPrediction():
    if request.method == "POST":
        print(request.files)
        file = request.files['image']
        utilObj = MlUtility(modelPath=modelPath)
        img = utilObj.loadImage(fileObj = file)
        img.save('test.png')
        imageArray = utilObj.preprocessImage(imgObj = img)
        cnn_model = utilObj.loadModel()
        prediction = utilObj.generatePrediction(model = cnn_model,imageArray = imageArray)
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
