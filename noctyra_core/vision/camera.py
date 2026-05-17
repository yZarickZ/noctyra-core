import cv2 as cv

class Camera:
    def __init__(self, index=0):
        self.cap = cv.VideoCapture(index)

    def read(self):
        return self.cap.read()

    def release(self):
        self.cap.release()