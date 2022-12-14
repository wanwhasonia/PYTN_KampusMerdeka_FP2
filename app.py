import numpy as np
import pandas as pd
from flask import Flask, render_template, request
import pickle

app=Flask(__name__)
model= pickle.load(open("svm.pkl", "rb"))

@app.route("/")
def home():
   return render_template('main.html')

@app.route("/predict", methods=["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    feature = [np.array(float_features)]
    prediction = model.predict(feature)
    output_svm = round(prediction[0], 2)
    output_text_svm = ''
    if (output_svm == 0):
        output_text_svm = 'No'
    elif (output_svm == 1):
        output_text_svm = 'Yes'
    return render_template("main.html", prediction_text= "Will it rain tomorrow? {}".format(output_text_svm))

if __name__=="__main__":
    app.run(debug=True)