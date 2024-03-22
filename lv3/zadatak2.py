import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv('data_C02_emission.csv')

plt.figure()
data['CO2 Emissions (g/km)'].plot(kind="hist", bins=20)
plt.show()


data['Fuel Type'] = data['Fuel Type'].astype('category')
colors = {'X': 'brown', 'D': 'black', 'Z': 'red', 'E': 'blue'}
data.plot.scatter(x="Fuel Consumption City (L/100km)", y="CO2 Emissions (g/km)", c=data["Fuel Type"].map(colors), s=30)
plt.show()


data.boxplot(column='CO2 Emissions (g/km)', by='Fuel Type')
plt.show()


fuel_grouped_num = data.groupby('Fuel Type').size()
fuel_grouped_num.plot(kind ='bar', xlabel='Vrsta goriva', ylabel='Broj vozila', title='Broj vozila po tipu goriva')
plt.show()


cylinder_grouped = data.groupby('Cylinders')['CO2 Emissions (g/km)'].mean()
cylinder_grouped.plot(kind='bar', x=cylinder_grouped.index, y=cylinder_grouped.values, xlabel='Cilindri', ylabel='CO2 emissions (g/km)', title='CO2 emisija vozila s obzirom na broj cilindara')
plt.show()