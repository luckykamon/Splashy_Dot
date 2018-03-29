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
    if k-j < 4 and k-j>-4:
      im[k,j]= [255, 0, 0]
    if 60 - k-j < 4 and 60-k-j>-4:
      im[k,j]= [255, 0, 0]

imageio.imsave("img2.jpg", im)

