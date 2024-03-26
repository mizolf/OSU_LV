import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
import sklearn.linear_model as lm
from sklearn.metrics import max_error
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OneHotEncoder


data = pd.read_csv('data_C02_emission.csv')

input = ['Fuel Type','Engine Size (L)','Cylinders','Fuel Consumption City (L/100km)','CO2 Emissions (g/km)']
output = 'CO2 Emissions (g/km)'

X = data[input]
y = data[output]

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state=1)

ohe = OneHotEncoder()
X_encoded_train = ohe.fit_transform(X_train[['Fuel Type']]).toarray()
X_encoded_test = ohe.fit_transform(X_test[['Fuel Type']]).toarray()

linearModel = lm.LinearRegression()
linearModel.fit(X_encoded_train, y_train)

y_test_p = linearModel.predict(X_encoded_test)

print(f"Max Error: {max_error(y_test, y_test_p)}")

error = np.abs(y_test_p, y_test)
print(np.max(error))
max_error_id = np.argmax(error)

print(data.iloc[max_error_id, 1])