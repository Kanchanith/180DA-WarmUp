'''
source:
- https://code.likeagirl.io/finding-dominant-colour-on-an-image-b4e075f98097
- https://docs.opencv.org/4.x/dc/da5/tutorial_py_drawing_functions.html
- https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
- https://docs.opencv.org/3.4/d3/df2/tutorial_py_basic_ops.html

'''
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
    focus = frame[300:800, 650:1250]
    rect = cv.rectangle(frame,(650,300),(1250,800),(0,255,0),3)

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