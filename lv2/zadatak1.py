import numpy as np
import matplotlib . pyplot as plt

x=np.array([3,3,2,1,3])
y=np.array([1,2,2,1,1])
plt.plot (x, y, 'b', linewidth =1, marker =".", markersize =10)
plt.axis ([0, 4, 0, 4])
plt.xlabel('x os')
plt.ylabel('y os')
plt.title('Primjer')
plt.show()