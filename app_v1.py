#import libraries 
import numpy as np
from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('model/model.pkl', 'rb'))

# on default page
@app.route('/')
def home():
    return render_template('index.html')

#To use the predit button
@app.route('/predict', methods=['post'])
def predict():
    #to render the results onto the HTML page
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0,2])
    return render_template('index.html', prediction_text = 'Thank you for submitting your details. Your credit risk is :{}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)

