import cv2
import imutils
import numpy as np

image = cv2.imread("level1.png")

# H, W = image.shape[:2]
# nilai = np.zeros((H, W), np.uint8
# image = imutils.resize(image, width=480)
cv2.imshow("test",image[:,:,0])
print("Avg of red           : ", np.average(image[:,:,2]))
print("Avg of green         : ", np.average(image[:,:,1]))
print("Avg of blue          : ", np.average(image[:,:,0]))
print("Sum of arr(uint8)    : ", np.sum(image, dtype=np.uint8))
print("Sum of arr(float32)  : ", np.sum(image, dtype=np.float32))
cv2.imshow("asli", image)
cv2.waitKey(0)