from flask import Flask, render_template, redirect, jsonify, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__, template_folder='templates')

# Use pickle to load in the pre-trained model.
with open(f'model/model.pkl', 'rb') as file:
    model = pickle.load(file)


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return(render_template('index.html'))
    if request.method == 'POST':
        annual_income = request.form['AMT_INCOME_TOTAL']
        age = request.form['AGE']
        occupation_type = request.form['OCCUPATION_TYPE']



        input_variables = pd.DataFrame([[annual_income, age, occupation_type, ]],
                                       columns=['annual_income', 'age', 'occupation_type'],
                                       dtype=float)
        prediction = model.predict(input_variables)[0]
        return render_template('index.html',
                                     original_input={ 'Annual Income': annual_income,
                                                    'Age': age,
                                                    'Occupation Type': occupation_type,
                                                    'Education Type': education_type,
                                                    'Months Employed': months_employed,
                                                    'Count Family': count_family,
                                                    'Income Type': income_type,
                                                    'Count of Children': count_children,
                                                    'Family Status':family_status,
                                                    'Own Car': own_car,
                                                    'Own Phone': phone,
                                                    'Own Realty': own_realty,
                                                    'Housing Type': housing_type,
                                                    'Gender': gender,
                                                    'Have Email': email

                                     },
                                     result=prediction,
                                     )
if __name__ == '__main__':
    app.run(debug=True)

