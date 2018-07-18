import cv2
import numpy as np

image = cv2.imread("image1.png")
cv2.imshow("ORIGINAL_IMAGE", image)
cv2.waitKey(0)

## GrayScale Conversion
gray = cv2.imread("imagge1.jpg", 0)

# now maskin the image
# converting all the coloours to black
# except those in white
ret, thresh1 = cv2.threshold(gray, 254, 255, cv2.THRESH_BINARY)

## Making the marks thicker ...
# By dialting
kernel = np.ones((7,7), np.uint8)
mask = cv2.dilate(thresh1, kernel, iterations = 1)
cv2.imwrite("masked_image1.png", mask)

restored = cv2.inpaint(image, mask, 3, cv2.INPAINT_TELEA)

cv2.imshow("RESTORED_IMAGE", restored)
cv2.waitKey(0)
