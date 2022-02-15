import numpy as np
from flask import Flask, request, jsonify, render_template
from tensorflow import keras
import xgboost as xgb
import autokeras as ak
import json
import sys
import os

#sys.path.append("/Desktop/Projects/springboard_final")
#sys.path.append(os.path.abspath('/Desktop/Projects/springboard_final'))



app = Flask(__name__)

bst = xgb.Booster()  # init model
bst.load_model('models/xgb_model.json')  


@app.route('/')
def home():
    #return render_template('index.html')
    return json.dumps({"Status": "OK"})

@app.route('/predict',methods=['POST'])
def predict():

    #int_features = [int(x) for x in request.form.values()]
    #int_features = [float(x) for x in request.form.values()]
    features = [x for x in request.form.values()]
    #int_features = [int(x) for x in request.form.values()]
    # features_list = []
    # for i in features:
    #     if i == ',':
    #         pass
    #     else:
    #         features_list.append(i)

    # bst = xgb.Booster()  # init model
    # bst.load_model('xgb_model.json')  
    # dtest = xgb.DMatrix(features[0:1])
    # prediction = bst.predict(dtest)
    # output = prediction[0]

    
    # output = features_list
    # # output = round(prediction[0], 2)

    # return render_template('index.html', prediction_text='Sales should be $ {}'.format(str(output)))
    return "hello2"
    

@app.route('/results',methods=['POST'])
def results():
    data = request.get_json(force=True)
    dtest = xgb.DMatrix(data)
    prediction = bst.predict(dtest)
    output = prediction[0]
    return str(output)

# BELOW WORKS
    # data = request.get_json(force=True)

    # keras_model = keras.models.load_model("model_keras", custom_objects=ak.CUSTOM_OBJECTS)
    # prediction = keras_model.predict(data)
    # output = prediction[0][0]
    # return str(output)




if __name__ == "__main__":
    #app.run(debug=True)
    app.run(debug=True, host='0.0.0.0')