import cv2
import numpy as np

def nothing(x):
    pass

def createbars():

    cv2.createTrackbar("H_l", "image", 0, 180, nothing)
    cv2.createTrackbar("H_h", "image", 0, 180, nothing)
    cv2.createTrackbar("S_l", "image", 0, 255, nothing)
    cv2.createTrackbar("S_h", "image", 0, 255, nothing)
    cv2.createTrackbar("V_l", "image", 0, 255, nothing)
    cv2.createTrackbar("V_h", "image", 0, 255, nothing)

cv2.namedWindow("image")
createbars()

lower = np.array([0, 0, 0])
upper = np.array([0, 0, 0])
"""
lower = np.array([25, 95, 65])
upper = np.array([65, 255, 255])
"""

while True:
    frame = cv2.imread("YellowStick.jpg")
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower[0] = cv2.getTrackbarPos("H_l", "image")
    upper[0] = cv2.getTrackbarPos("H_h", "image")
    lower[1] = cv2.getTrackbarPos("S_l", "image")
    upper[1] = cv2.getTrackbarPos("S_h", "image")
    lower[2] = cv2.getTrackbarPos("V_l", "image")
    upper[2] = cv2.getTrackbarPos("V_h", "image")

    mask = cv2.inRange(hsv_frame, lower, upper)
    cv2.imshow("mask", mask)
    if cv2.waitKey(0):
        break
cv2.destroyAllWindows()