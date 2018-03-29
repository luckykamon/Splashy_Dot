import imageio
import matplotlib.pyplot as plt
import Image
import numpy as np

im = Image.new("RGB", (60, 60), "white")
pic = np.array(im)
im=pic
rayon = 15
epaisseur = 3
for k in range(60):
  for j in range(60):
    if (k-30)*(k-30) + (j-30)*(j-30) < rayon * rayon and (k-30)*(k-30) + (j-30)*(j-30) > (rayon - epaisseur) * (rayon - epaisseur):
      im[k,j]= [230, 0, 0]

imageio.imsave("img2.jpg", im)

