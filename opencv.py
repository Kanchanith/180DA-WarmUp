import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # rect = cv2.rectangle(frame,(384,0),(510,128),(0,255,0),3)

    # Range of pink
    hsv_lower_green = np.array([50,90,90])
    hsv_upper_green = np.array([70,255,255])

    bgr_lower_green = np.array([2,128,2])
    bgr_upper_green = np.array([121,255,121])

    # Applying the threshold to isolate the pink object
    # mask = cv.inRange(img, brg_lower_pink, brg_upper_pink)
    mask = cv.inRange(hsv, hsv_lower_green, hsv_upper_green)

    contours, hierarchy = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    if (len(contours) > 0):
        # c = contours[0]
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



# import numpy as np
# import cv2 as cv
# img = cv.imread('airpods.jpeg')
# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# green = np.uint8([[[0,255,0 ]]])
# hsv_green = cv.cvtColor(green,cv.COLOR_BGR2HSV)
# print( hsv_green )
# pink = np.uint8([[[2,128,2]]])
# print(cv.cvtColor(pink,cv.COLOR_BGR2HSV))
# BGR 137, 134, 186  HSV 178 71 186






# ret, thresh = cv.threshold(imgray, 150, 200, cv.THRESH_BINARY)
# contours, hierarchy = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
# cnt = max(contours, key = cv.contourArea)
# x,y,w,h = cv.boundingRect(cnt)
# cont_img = cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)
# # cont_img = cv.drawContours(img, contours, -1, 255, 3)
# cv.imshow('im', cont_img)
# cv.waitKey(0)

