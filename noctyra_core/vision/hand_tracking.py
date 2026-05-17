"""
Noctyra Core - Hand Tracking Module

Responsible for:
- MediaPipe hand detection
- Landmark processing
- Hand landmark rendering
"""

# Import OpenCV
import cv2 as cv

# Import MediaPipe
import mediapipe as mp


# Hand tracking abstraction class
class HandTracker:

    # Constructor method
    def __init__(self):

        # MediaPipe hand solution module
        self.mp_hands = mp.solutions.hands

        # MediaPipe drawing utilities
        self.mp_draw = mp.solutions.drawing_utils

        # Initialize the hand tracking system
        self.hands = self.mp_hands.Hands(

            # False = optimized for real-time video processing
            static_image_mode=False,

            # Maximum number of detectable hands
            max_num_hands=2,

            # Minimum confidence required for hand detection
            min_detection_confidence=0.5,

            # Minimum confidence required for hand tracking
            min_tracking_confidence=0.5
        )

    # Process a frame and detect hands
    def process(self, frame):

        # Convert BGR to RGB
        # OpenCV uses BGR by default
        # MediaPipe expects RGB input
        frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

        # Process the frame using MediaPipe
        results = self.hands.process(frame_rgb)

        # Check if hands were detected
        if results.multi_hand_landmarks:

            # Iterate through each detected hand
            for hand_landmarks in results.multi_hand_landmarks:

                # Draw landmarks and hand connections
                self.mp_draw.draw_landmarks(

                    # Original frame
                    frame,

                    # Hand landmark data
                    hand_landmarks,

                    # Landmark connection structure
                    self.mp_hands.HAND_CONNECTIONS
                )

        # Return:
        # - Processed frame
        # - Raw MediaPipe results
        return frame, results