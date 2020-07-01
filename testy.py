import cv2
import numpy as np
import imutils

asli = cv2.imread("banyak1.jpg")
# asli = imutils.resize(asli, width=480)
# cv2.imshow("Asli", asli)
image = asli
hsv_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

# darkorange = np.array([20, 98, 115])
darkorange = np.array([57, 14, 98])
lightorange = np.array([179, 255, 255])
# lightorange = np.array([26, 76, 91])

mask_orange = cv2.inRange(hsv_image, darkorange,lightorange)

ret,thresh = cv2.threshold(mask_orange, 40, 255, 0)
im, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

hasil = cv2.bitwise_and(image, image, mask=mask_orange)

jum = 0
for i in contours :
    jum += 1

largest_area = 0
largest_area_index = 0
for i in range(jum):
     area = cv2.contourArea(contours[i])
     if area > largest_area :
         largest_area = cv2.contourArea(contours[i])
         largest_area_index = i

M = cv2.moments(contours[largest_area_index])
cX = int(M["m10"] / M["m00"])
cY = int(M["m01"] / M["m00"])

# print(cX,cY)
# print(asli.shape)
sample = np.zeros((20, 20, 3), dtype=np.uint8)
x = 0
for i in range(20):
    for n in range(20):
        sample[i,n] = (asli[cY-10+n,cX-10+i])

cv2.drawContours(image, contours[largest_area_index], -1, 255, 3)
cv2.rectangle(image,(cX-11,cY - 11),(cX+11,cY + 11),(255, 255, 255),1 )
cv2.circle(image,(cX,cY),1,(255, 255, 255),-1 )
cv2.putText(image,"Titik Sample",(cX - 20, cY - 20),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

gray_sample = cv2.cvtColor(sample,cv2.COLOR_BGR2GRAY)
# sample = cv2.GaussianBlur(sample,(3,3),cv2.BORDER_DEFAULT)
print(gray_sample)
print("Avg of red           : ", np.average(sample[:, :, 2]))
print("Avg of green         : ", np.average(sample[:, :, 1]))
print("Avg of blue          : ", np.average(sample[:, :, 0]))
print("Avg Gray value = ", np.average(sample))
hsv_sample = cv2.cvtColor(sample,cv2.COLOR_BGR2HSV)
# print(sample)

hasil2 = imutils.resize(hasil, width=480)
image2 = imutils.resize(image, width=480)
sample = imutils.resize(sample, width=480)


cv2.imshow("cupikan", sample)
cv2.imshow("Hasil", image2)
cv2.waitKey(0)