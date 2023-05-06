import cv2
import mediapipe as mp
import math
import pyttsx3

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Load pose estimation model
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    # Start camera stream
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        # Read frame from camera
        success, image = cap.read()
        if not success:
            print("Failed to read camera stream")
            break

        # Convert image to RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Process image with pose estimation model
        results = pose.process(image)

        # Calculate distance between shoulder and hip joints
        shoulder_x = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].x
        shoulder_y = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].y
        hip_x = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP].x
        hip_y = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP].y

        distance = math.sqrt((hip_x - shoulder_x) ** 2 + (hip_y - shoulder_y) ** 2)

        # Classify driver based on seatbelt distance
        if distance < 0.2:
            print("Driver is wearing a seatbelt")
            engine.say("Driver is wearing a seatbelt")
        else:
            print("Driver is not wearing a seatbelt")
            engine.say("Driver is not wearing a seatbelt")

        # Draw pose landmarks on image
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Show image
        cv2.imshow("Pose Estimation", image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    
    # Shut down the text-to-speech engine
    engine.stop()
