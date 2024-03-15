import numpy as np
import matplotlib . pyplot as plt

img = plt.imread ("road.jpg")
img = img[:,:,0].copy()
plt.figure ()
plt.title("Posvjetljena slika")
plt.imshow(img, cmap ="gray", alpha=0.5)
plt.show()

plt.title("Druga 1/4 slike")
width = len(img[0])
quarter = int(width/4)
plt.imshow(img[:, quarter: 2*quarter], cmap="gray")
plt.show()

plt.title("Rotirana slika za 90 stupnjeva")
plt.imshow(np.rot90(img, 3), cmap="gray")
plt.show()

plt.title("Zrcaljena slika")
plt.imshow(np.flip(img, 0), cmap="gray")
plt.show()