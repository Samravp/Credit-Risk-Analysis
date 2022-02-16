# Credit Approval Prediction

## Project Name: Can I Borrow App

## Slogan: "Your Reliable Loan Application Outcome Predictor"

This application was created using a machine learning model to predict if a credit card/loan application will get approved or not using supervised learning with scikit-learn and data manipulation with pandas.

Can I Borrow aims to provide a reliable and free tool for individuals to predict their credit risk and if their loan application will approved.

Please see the application deployed on Heroku [here](https://caniborrow22.herokuapp.com/).

## Team Members  👨🏻‍💻👩🏻‍💻👩🏻‍💻👩🏻‍💻

- [Dylan McKibbin](https://github.com/macadyls)
- [Ishaan Nigam](https://github.com/ishaan04)
- [Nga Phu](https://github.com/nkphu)
- [Samra Vatan Parast](https://github.com/Samravp)



## Datasets

We obtained our data from Kaggle, we used [Credit Card Approval Prediction Dataset](https://www.kaggle.com/rikdifos/credit-card-approval-prediction). 

Second dataset that we used was Australia Bureau of Statistics's [Household Income and Wealth Dataset](https://www.abs.gov.au/statistics/economy/finance/household-income-and-wealth-australia/latest-release)

This dataset provides below information:
- Household debt across Australia
- Household debt by age
- Trend of household debt from 2003 – 2018
- How does Australia’s household debt compare to other countries

And the last dataset was Organisation for Economic Cooperation and Development's [Household Debt Dataset](https://data.oecd.org/hha/household-debt.htm)

## ETL Process

* **Extract**:Datasets were exported from abovementioned sources.

* **Transform**: Using Jupyter Notebook and pandas, we cleaned and reorganised the data according to our needs.

* **Load**: Considering the normalised and relational structure of our data, PostgreSQL would have been our database of choice, however, due to time constraints we skipped databasing step.

## Machine Learning (ML)

For the machine learning part of this project, we used below libraries;

- DecisionTreeClassifier
- RandomForests 
- XGBoost 
- KNeighborsClassifier
- LogisticRegression 
- SVC Classifier
- LightGBM 
- Catboost

In terms of accuracy, the most accurate ML model was XGBoost with 92% accuracy.

Least accurate ML model was KNeighbours with 48% accuracy.

For the purpose of this project, we decided to proceed with LightGBM model with 90% accuracy.

Although XGBoost is higher at 92%, the weighting of the features were not justifiable.


## Data Visualisation

We draw insights from our data using Tableau, Python's Seaborn library in Jupyter Notebook and SciKit-learn for machine learning visualisations.


## Final Dashboard

 <p align="center">
<img width="1234" alt="Webpage" src="https://user-images.githubusercontent.com/85004202/154185072-52e11ca1-b0f2-488f-85f6-403c4e5e4f30.png">
 </p>
