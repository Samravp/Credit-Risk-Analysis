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
        annual_income = request.form['AMT_INCOME_TOTAL']
        age = request.form['AGE']
        occupation_type = request.form['OCCUPATION_TYPE']
        education_type = request.form['NAME_EDUCATION_TYPE']
        months_employed = request.form['MONTHS_EMPLOYED']
        count_family = request.form['CNT_FAM_MEMBERS']
        income_type = request.form['NAME_INCOME_TYPE']
        count_children = request.form['CNT_CHILDREN']
        family_status = request.form['NAME_FAMILY_STATUS']
        own_car = request.form['FLAG_OWN_CAR']
        phone = request.form['FLAG_PHONE']
        own_realty = request.form['FLAG_OWN_REALTY']
        housing_type = request.form['NAME_HOUSING_TYPE']
        gender = request.form['CODE_GENDER']
        email = request.form['FLAG_EMAIL']


        input_variables = pd.DataFrame([[annual_income, age, occupation_type, education_type, months_employed, count_family, income_type, count_children, family_status, own_car, phone, own_realty, housing_type, gender, email]],
                                       columns=['annual_income', 'age', 'occupation_type', 'education_type', 'months_employed', 'count_family', 'income_type', 'count_children', 'family_status', 'own_car', 'phone', 'own_realty', 'housing_type', 'gender', 'email'],
                                       dtype=float)
        prediction = model.predict(input_variables)[0]

        return render_template('index.html', prediction_text = 'Thank you for submitting your details. Your credit risk is : {}'.format(prediction))

if __name__ == '__main__':
    app.run(debug=True)
