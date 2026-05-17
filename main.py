"""
Noctyra Core - Main Application

Responsible for:
- Capturing frames from the camera
- Processing hand tracking
- Rendering the final output
"""

# Import OpenCV library
import cv2 as cv

# Import the camera abstraction module
from noctyra_core.vision.camera import Camera

# Import the hand tracking system
from noctyra_core.vision.hand_tracking import HandTracker


# Create a camera object using the default webcam (index 0)
camera = Camera(0)

# Create the hand tracking object
tracker = HandTracker()


# Main application loop
while True:

    # Read the current frame from the camera
    success, frame = camera.read()

    # Check if the frame was captured successfully
    if not success:
        print("Failed to read camera frame.")
        break

    # Process the frame using MediaPipe hand tracking
    # Returns:
    # - Processed frame
    # - Tracking results
    frame, results = tracker.process(frame)

    # Display the processed frame in a window
    cv.imshow("Noctyra Camera", frame)

    # Wait 1 millisecond for keyboard input
    # ASCII 27 = ESC key
    if cv.waitKey(1) == 27:
        break


# Release the camera resource
camera.release()

# Close all OpenCV windows
cv.destroyAllWindows()