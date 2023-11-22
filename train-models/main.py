from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from google.oauth2 import service_account
from google.cloud import bigquery
import pandas as pd
import joblib

creds = service_account.Credentials.from_service_account_file('mineria2023-30.json')
client = bigquery.Client(credentials=creds, project='mineria2023-30')

sql = "SELECT * FROM `mineria2023-30.mineria_07262023.Clientes_IMP`"
df_data = client.query(sql).result().to_dataframe()

inputs = ['Ind__Pr__stamo', 'Ind__Salario', 'Ind__Formaci__n'] + ['Score_Cliente']
df_ = df_data[inputs]
df_.columns = ['ind_prestamo', 'ind_salario', 'ind_formacion', 'score']

X = df_[['ind_prestamo', 'ind_salario', 'ind_formacion']]
y = df_['score']

Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.3, random_state=10)
lr = LinearRegression()
lr.fit(Xtrain, ytrain)
lr.score(Xtest, ytest)
ypred = lr.predict(Xtest)

df_result = pd.DataFrame(Xtest)
ypred.shape
df_result['score_pred'] = ypred

joblib.dump(lr,'../models/model_score.joblib')