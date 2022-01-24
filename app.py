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
        return(render_template('index.html'))
    if request.method == 'POST':
        input_list = request.form.to_dict()
        for key, value in input_list.items():
            try:
                input_list[key] = [int(value)]
            except ValueError:
                input_list[key] = float(value) 
        
        input_df = pd.DataFrame(input_list) 

        print(input_df)

        result = Predictor(input_df)
        if int(result)==1:
            prediction='High'
        else:
            prediction='Low'
        return render_template("index.html",prediction_text = 'Thank you for submitting your details. Your credit risk is : {}'.format(prediction))

def Predictor(input_df):
    # print(input_list)
    # to_predict = np.array(input_list).reshape(1,15)
    
    # call scaler on dataframe

    with open(f'model/scalar.pkl', 'rb') as file:
        scaler = pickle.load(file)

    result_df = scaler.transform(input_df)
    print(result_df)

    result = model.predict(result_df)
    return result[0]

if __name__ == '__main__':
    app.run(debug=True)