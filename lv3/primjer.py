import pandas as pd
import matplotlib . pyplot as plt
data = pd. read_csv ('data_C02_emission.csv')

data . boxplot ( column =['CO2 Emissions (g/km)'], by='Cylinders')
plt . show ()