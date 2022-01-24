from flask import Flask, render_template, redirect, jsonify, request
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__, template_folder='templates')

# Use pickle to load in the pre-trained model.
with open(f'model/model.pkl', 'rb') as file:
    model = pickle.load(file)


@app.route('/', methods=['GET', 'POST'])

def main():
    if request.method == 'GET':
        return(render_template('newform.html'))
    if request.method == 'POST':
        input_list = request.form.to_dict()
        input_list = list(input_list.values())
        input_list = list(map(int, input_list))
        result = Predictor(input_list)
        if int(result)==1:
            prediction='High'
        else:
            prediction='Low'
        return render_template("newform.html",prediction_text = 'Thank you for submitting your details. Your credit risk is : {}'.format(prediction))

def Predictor(input_list):
    to_predict = np.array(input_list).reshape(1,15)
    result = model.predict(to_predict)
    return result[0]

if __name__ == '__main__':
    app.run(debug=True)