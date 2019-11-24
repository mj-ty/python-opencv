import cv2
import numpy as np

frame = cv2.imread("YellowStick.jpg")
hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

lower = np.array([25, 95, 65])
upper = np.array([65, 255, 255])

mask = cv2.inRange(hsv_frame, lower, upper)
contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
x, y, w, h = cv2.boundingRect(contours[0])
img = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

cx = x + w/2
cy = y + h/2
print(x, y, w, h)
print(cx, cy)

cv2.imshow("text", mask)
cv2.imshow("text1", img)

cv2.waitKey(0)
cv2.destroyAllWindows()