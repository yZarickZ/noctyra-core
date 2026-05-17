"""
Noctyra Core - Camera Module

Responsible for:
- Camera initialization
- Frame capture
- Camera resource management
"""

# Import OpenCV
import cv2 as cv


# Camera abstraction class
class Camera:

    # Constructor method
    # Automatically runs when creating the object
    def __init__(self, index=0):

        # Initialize webcam capture
        # index=0 usually refers to the main/default camera
        self.cap = cv.VideoCapture(index)

    # Read a frame from the camera
    def read(self):

        # Returns:
        # - success status (True/False)
        # - captured frame
        return self.cap.read()

    # Release the camera resource
    def release(self):

        # Frees the webcam so other applications can use it
        self.cap.release()