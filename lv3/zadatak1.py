import pandas as pd
data = pd. read_csv ('data_C02_emission.csv')

print("DataFrame mjerenja: ", len(data['Make']))

for col in data.columns:
    print(f"{col} je tipa {data[col].dtype}")

print("Izostale vrijednosti: ",data.isnull().sum())
print("Duplicirane vrijednosti: ",data.duplicated().sum())

data['Vehicle Class'] = data['Vehicle Class'].astype('category')


max_consume = data.nlargest(3, 'Fuel Consumption City (L/100km)')
print('Najveća potrošnja: ')
print(max_consume[['Make', 'Model', 'Fuel Consumption City (L/100km)']])

min_consume = data.nsmallest(3, 'Fuel Consumption City (L/100km)')
print('Najmanja potrošnja: ')
print(min_consume[['Make', 'Model', 'Fuel Consumption City (L/100km)']])


temp = data[(data['Engine Size (L)'] >= 2.5) & (data['Engine Size (L)'] <= 3.5)]
print("Vozila koji imaju motor izmedu 2.5 i 3.5 L: ",len(temp['Make']))
print("Prosjecna C02 emisija ovih vozila jest: ",temp['CO2 Emissions (g/km)'].mean(), "g/km")


temp = data[(data['Make'] == 'Audi')]
print(f"U mjerenjima ima {len(temp['Make'])} mjerenja koja se odnose na marku Audi")

temp = temp[(temp['Cylinders'] == 4)]
print(f"Prosjecna CO2 emisija marke Audi s 4 cilindara je {temp['CO2 Emissions (g/km)'].mean()} g/km")


cylinder_counts = data['Cylinders'].value_counts().sort_index()
print(cylinder_counts)

cylinder_emissions = data.groupby('Cylinders')['CO2 Emissions (g/km)'].mean()
print("Cylinder emissions: ")
print(cylinder_emissions)


diesels = data[(data['Fuel Type'] == 'D')]
benzin = data[(data['Fuel Type'] == 'Z')]

print("Prosječna potrošnja vozila koji koriste dizel: ",diesels['Fuel Consumption City (L/100km)'].mean())
print("Prosječna potrošnja vozila koji koriste benzin: ",benzin['Fuel Consumption City (L/100km)'].mean())
print("Medijalne vrijednosti: ",diesels['Fuel Consumption City (L/100km)'].median())
print("Medijalne vrijednosti: ",benzin['Fuel Consumption City (L/100km)'].median())


four_cylinder_diesels = diesels[(diesels['Cylinders'] == 4)]
print(f"Najveća gradska potrošnja vozila s 4 cilindra:\n{four_cylinder_diesels.nlargest(1, 'Fuel Consumption City (L/100km)')}")


manuals = data[(data['Transmission'].str[0] == 'M')]
print(f"Postoji {len(manuals['Make'])} vozila s rucnim mjenjacem.")


print(data.corr(numeric_only=True))

'''
Veličine u datom skupu podataka su značajno povezane. Na primer, broj cilindara i zapremina motora imaju korelacijski koeficijent oko 0,9, dok je potrošnja goriva povezana sa koeficijentom oko 0,8, što ukazuje na snažnu međusobnu povezanost.
Treba imati na umu da potrošnja goriva koja je izražena u miljama po galonu (MPG) ima veliku negativnu korelaciju jer je obrnuto proporcionalna veličina. Što vozilo troši više goriva, MPG broj je manji.
Na primer, vozilo koje troši 25 MPG troši više goriva od vozila koje troši 45 MPG. Zbog ove obrnuto proporcionalne veze, koja se može izraziti kao litre na 100 kilometara (L/100 km), rezultira negativnom korelacijom. 
Što je negativni korelacijski koeficijent bliži -1, to je obrnuta proporcionalnost veća.
'''