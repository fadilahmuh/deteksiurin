import cv2
import imutils
import numpy as np

for i in range(1,9):
    file = "Level indikator%s.png"%(i)
    image = cv2.imread(file)
    print(file)
    print("Avg of red           : ", np.average(image[:, :, 2]))
    print("Avg of green         : ", np.average(image[:, :, 1]))
    print("Avg of blue          : ", np.average(image[:, :, 0]))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print("Avg of gray          : ", np.average(image))
    print("===================================================")