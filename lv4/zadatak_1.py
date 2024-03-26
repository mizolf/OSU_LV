import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
import sklearn.linear_model as lm
from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_absolute_percentage_error, r2_score
from sklearn.preprocessing import MinMaxScaler


data = pd.read_csv('data_C02_emission.csv')
input = ['Engine Size (L)','Cylinders','Fuel Consumption City (L/100km)','CO2 Emissions (g/km)']
output = 'CO2 Emissions (g/km)'
X = data[input]
y = data[output]
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state=1)


plt.scatter(X_train['Fuel Consumption City (L/100km)'], y_train, c='Blue')
plt.scatter(X_test['Fuel Consumption City (L/100km)'], y_test, c='Red')
plt.xlabel('Fuel Consumption City (L/100km)')
plt.ylabel('CO2 Emissions (g/km)')
plt.title('Gradska potrošnja uspoređena s veličinom motora')
plt.show()


plt.hist(X_train['Cylinders'])
plt.show()
sc = MinMaxScaler()
X_train_n = sc.fit_transform(X_train)
plt.hist
plt.hist(X_train_n[:, 0])
plt.show()
X_test_n = sc.transform(X_test)


linearModel = lm.LinearRegression()
linearModel.fit(X_train_n, y_train)
print(linearModel.coef_)


y_test_p = linearModel.predict(X_test_n)
plt.scatter(y_test, y_test_p)
plt.title("Stvarne vrijednosti izlaznih veličina u odnosu na procjenu izlaznih veličina")
plt.xlabel("Stvarne vrijednosti izlaznih veličina")
plt.ylabel("Procjena izlaznih veličina")
plt.show()


MAE = mean_absolute_error(y_test , y_test_p)
MSE = mean_squared_error(y_test , y_test_p)
MAPE = mean_absolute_percentage_error(y_test, y_test_p)
RMSE = mean_squared_error(y_test, y_test_p, squared=False)
R_2 = r2_score(y_test, y_test_p)

print(f"MAE: {MAE}\nMSE: {MSE}\nMAPE: {MAPE}\nRMSE: {RMSE}\nR2 SCORE: {R_2}")


'''
Mijenjanje broja ulaznih veličina može utjecati na metriku procjene na različite načine. 
Pažljiv odabir ulaznih varijabli ključan je za postizanje optimalne izvedbe.
'''