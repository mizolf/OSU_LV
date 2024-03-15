import numpy as np
import matplotlib . pyplot as plt

zeros=np.zeros((50,50))
ones=np.ones((50,50))

top = np.hstack((zeros, ones))
bottom = np.hstack((ones, zeros))

plt.figure()
plt.imshow(np.vstack((top, bottom)), cmap="gray")
plt.show()
