import mediapipe as mp
import cv2
import math

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

def is_driver_looking_at_road(face_landmarks):
    horizontal_threshold = 15
    vertical_threshold = 15
    
    left_eye_x = face_landmarks.landmark[33].x
    left_eye_y = face_landmarks.landmark[33].y
    right_eye_x = face_landmarks.landmark[263].x
    right_eye_y = face_landmarks.landmark[263].y
    
    if abs(left_eye_y - right_eye_y) <= horizontal_threshold and abs(left_eye_x - right_eye_x) <= vertical_threshold:
        return True
    return False

def is_driver_holding_steering_wheel(left_hand_landmarks, right_hand_landmarks):
    if left_hand_landmarks and right_hand_landmarks:
        left_hand_y = left_hand_landmarks.landmark[0].y
        right_hand_y = right_hand_landmarks.landmark[0].y
        steering_wheel_height_threshold = 0.05

        if abs(left_hand_y - right_hand_y) <= steering_wheel_height_threshold:
            return True
    return False

def is_driver_maintaining_posture(pose_landmarks):
    left_shoulder = pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_SHOULDER.value]
    right_shoulder = pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_SHOULDER.value]
    left_hip = pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_HIP.value]
    right_hip = pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_HIP.value]

    shoulder_line = abs(left_shoulder.y - right_shoulder.y)
    hip_line = abs(left_hip.y - right_hip.y)

    threshold = 0.05

    if shoulder_line <= threshold and hip_line <= threshold:
        return True
    return False

cap = cv2.VideoCapture(0)

with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    
    while cap.isOpened():
        ret, frame = cap.read()
        
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = holistic.process(image)
        
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        if results.face_landmarks:
            mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACEMESH_TESSELATION)
            
            if is_driver_looking_at_road(results.face_landmarks):
                cv2.putText(image, "Driver looking at the road", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            else:
                cv2.putText(image, "Driver NOT looking at the road", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        
        if results.right_hand_landmarks:
            mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
        
        if results.left_hand_landmarks:
            mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
        
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)
            
            if is_driver_maintaining_posture(results.pose_landmarks):
                cv2.putText(image, "Driver maintaining proper posture", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            else:
                cv2.putText(image, "Driver NOT maintaining proper posture", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        
        if is_driver_holding_steering_wheel(results.left_hand_landmarks, results.right_hand_landmarks):
            cv2.putText(image, "Driver holding the steering wheel properly", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        else:
            cv2.putText(image, "Driver NOT holding the steering wheel properly", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        
        cv2.imshow('Raw Webcam Feed', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()


           
    