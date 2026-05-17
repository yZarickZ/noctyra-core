import cv2 as cv
from noctyra_core.vision.camera import Camera
from noctyra_core.vision.hand_tracking import HandTracker

camera = Camera(0)
tracker = HandTracker()

while True:
    success, frame = camera.read()

    if not success:
        print("Failed to read camera frame.")
        break

    frame, results = tracker.process(frame)

    cv.imshow("Noctyra Camera", frame)

    if cv.waitKey(1) == 27:
        break

camera.release()
cv.destroyAllWindows()