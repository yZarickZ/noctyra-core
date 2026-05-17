import numpy as np
import cv2 as cv

camera = cv.VideoCapture(0)

while True:

    success, frame = camera.read()

    cv.imshow("Camera", frame)

    if cv.waitKey(1) == 27:
        break

camera.release()
cv.destroyAllWindows()