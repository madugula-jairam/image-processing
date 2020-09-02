
import cv2 
from matplotlib import pyplot as plt


img = cv2.imread('lena.jpg')
b,g,r = cv2.split(img)

plt.imshow(img),plt.title("Original"), plt.show()
plt.imshow(r),plt.title("RED"), plt.show()
plt.imshow(g),plt.title("Green"), plt.show()
plt.imshow(b),plt.title("Blue"), plt.show()

img2 = cv2.merge((r,g,b))
plt.imshow(img2)
plt.title("Merge image")
plt.show()
