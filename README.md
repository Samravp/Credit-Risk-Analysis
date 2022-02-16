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

Using Tableau Embed Code, we embeded below dashboard in our webpage.

 <p align="center">
 <img width="1280" alt="Tableau" src="https://user-images.githubusercontent.com/85004202/154185423-1aac42e1-4ee0-42fd-a130-0135abc19a79.png">
 </p>


## User Interactivity

After visiting the webpage and reading the informations, users could complete an online form via Heroku that calculates their risk level to get loan approval.

Please see below screenshots of the final webpage and online form.


## Final Web Dashboard

 <p align="center">
<img width="1234" alt="Webpage" src="https://user-images.githubusercontent.com/85004202/154185072-52e11ca1-b0f2-488f-85f6-403c4e5e4f30.png">
 </p>
 
 <p align="center">
<img width="1234" alt="Seaborn Visuals " src="https://user-images.githubusercontent.com/85004202/154185676-352697b8-3d6b-4b88-9a96-0f12e3855b51.png">
 </p>

 <p align="center">
<img width="1234" alt="Data viz 2" src="https://user-images.githubusercontent.com/85004202/154185860-7f63adc5-ff70-496d-92ff-4b39e9ca000f.png">
 </p>
 
 <p align="center">
<img width="1234" alt="Web page - about us" src="https://user-images.githubusercontent.com/85004202/154186326-70215641-c383-4321-bb2a-31d1ead7883b.png">
 </p>




### Heroku App

 <p align="center">
 <img width="1256" alt="Heroku" src="https://user-images.githubusercontent.com/85004202/154186023-fee1225a-1bbe-4762-af4b-87fcfd3bff27.png">
 </p>
