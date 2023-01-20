import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert frame color from BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Range of green
    hsv_lower_green = np.array([50,90,90])
    hsv_upper_green = np.array([70,255,255])

    bgr_lower_green = np.array([2,128,2])
    bgr_upper_green = np.array([121,255,121])

    # Applying the threshold to isolate the object
    mask = cv.inRange(frame, bgr_lower_green, bgr_upper_green)
    # mask = cv.inRange(hsv, hsv_lower_green, hsv_upper_green)
    contours, hierarchy = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    if (len(contours) > 0):
        c = max(contours, key = cv.contourArea)
        x,y,w,h = cv.boundingRect(c)
        cont_img = cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),5)
        # cont_img = cv.drawContours(frame, contours, -1, 255, 3)

    # Display the resulting frame
    cv.imshow('frame',frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()

