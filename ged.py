import numpy as np
import cv2
img = cv2.imread('mungkin sehat2.jpg',0)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)
print("rata-rata gray  : ", np.average(cl1))
# cv2.imwrite('hasil',cl1)