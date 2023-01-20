import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

cap = cv.VideoCapture(0)

# a matrix of RGB
bar = np.zeros((50, 300, 3), dtype="uint8")

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert color from BGR to RGB
    RGB_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    # Draw a rectangle and apply Image ROI
    rect = cv.rectangle(frame,(650,300),(1250,800),(0,255,0),3)
    focus = frame[650:1250, 300:800]

    # 3D to 2D
    focus = focus.reshape((focus.shape[0] * focus.shape[1],3))

    # Apply kmeans
    clt = KMeans(n_clusters=1) #cluster number
    clt.fit(focus)

    # Transfer RGB value of dominant color to list
    bar[:] = clt.cluster_centers_[0]

    # # Display the resulting frame
    cv.imshow('frame', frame)
    cv.imshow('dominant color',bar)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()