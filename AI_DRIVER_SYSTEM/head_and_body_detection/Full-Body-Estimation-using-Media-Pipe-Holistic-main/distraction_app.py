import streamlit as st
import mediapipe as mp
import cv2
import numpy as np
import pyttsx3
from PIL import Image

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

def is_driver_distracted(pose_landmarks):
    if pose_landmarks is None:
        return False

    # Get the landmarks for the head and neck
    nose = pose_landmarks.landmark[mp_holistic.PoseLandmark.NOSE]
    left_eye = pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_EYE]
    right_eye = pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_EYE]

    # Calculate the head tilt angle
    angle = np.arctan2(right_eye.y - left_eye.y, right_eye.x - left_eye.x) * 180 / np.pi

    # If the head tilt angle is more than 15 degrees, consider it a distraction
    if abs(angle) > 15:
        return True

    return False

def speak_alert():
    engine = pyttsx3.init()
    engine.setProperty('rate', 125)
    engine.say("Focus!")
    engine.runAndWait()

def main():
    st.title("Driver Protection System")

    st.sidebar.title("Configuration")
    st.sidebar.markdown("Configure the parameters of the driver protection system.")

    run_button = st.sidebar.button("Run")
    if run_button:
        st.write("Running the driver protection system...")
        st.write("Press 'q' to stop.")

        cap = cv2.VideoCapture(0)

        with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:

            while cap.isOpened():
                ret, frame = cap.read()

                # Recolor Feed
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Make Detections
                results = holistic.process(image)

                # Recolor image back to BGR for rendering
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                # Draw face landmarks
                mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACEMESH_TESSELATION)

                # Right hand
                mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

                # Left Hand
                mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

                # Pose Detections
                mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)

                # Analyze the pose landmarks for driver distraction
                if is_driver_distracted(results.pose_landmarks):
                    # Draw "FOCUS!" text on the image
                    cv2.putText(image, 'FOCUS!', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

                    # Speak the "Focus" alert
                    speak_alert()

                # Display the image in the web app
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                image_pil = Image.fromarray(image)
                st.image(image_pil, channels="RGB", use_column_width=True)

                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break

        cap.release()

    else:
        st.write("Press 'Run' to start the driver protection system.")
