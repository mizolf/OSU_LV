import numpy as np
import matplotlib . pyplot as plt

data=np.loadtxt('data.csv', delimiter=",", dtype="str")
data=data[1::]
print(f"Na {len(data)} osoba je izvršeno mjerenje")

data=np.array(data, np.float64)
height=data[:,1]
weight=data[:,2]
plt.scatter(height, weight)
plt.show()


avgHeight = height.mean()
maxHeight = height.max()
minHeight = height.min()
print(f"Maksimalna visina: {maxHeight} \nMinimalna visina: {minHeight} \nProsječna visina: {avgHeight}")

height=data[0::50,1]
weight=data[0::50,2]
plt.scatter(height, weight)
plt.show()

ind=(data[:,0] == 1)
men = data[ind]
women = data[ind!=1]
print(f"Muškarci:\n Maksimalna visina: {men[:, 1].max()}, Minimalna visina: {men[:, 1].min()}, Prosječna visina: {men[:, 1].mean()}")
print(f"Žene:\n Maksimalna visina: {women[:, 1].max()}, Minimalna visina: {women[:, 1].min()}, Prosječna visina: {women[:, 1].mean()}")