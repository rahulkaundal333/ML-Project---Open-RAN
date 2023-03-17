from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        PRB_usage= int(request.form['PRB usage'])
        MCS=int(request.form['MCS'])
        RRC_conn_UE=int(request.form['RRC conn UE'])
        prediction=model.predict([[PRB_usage,RRC_conn_UE,MCS]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you cannot calculate throughput")
        else:
            return render_template('index.html',prediction_text="Throughput is {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

