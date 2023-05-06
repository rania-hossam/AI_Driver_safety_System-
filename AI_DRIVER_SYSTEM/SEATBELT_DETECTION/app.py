import cv2
import mediapipe as mp
from threading import Thread
from playsound import playsound
import time

# Initialize the Mediapipe hand detection model
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
)

# Load the sound file for the alert
alert_sound = "C:\\Users\\rania\\Downloads\\AI_DRIVER_SYSTEM\\hand_steerwheeling_detection\\alarm.mp3"

# Initialize the OpenCV video capture object
cap = cv2.VideoCapture(0)

# Initialize the window for displaying the video stream
cv2.namedWindow("Hands on the Steering Wheel Detection", cv2.WINDOW_NORMAL)

# Define a function for playing the alert sound
def play_alert_sound():
    playsound(alert_sound)

# Set a delay of 5 seconds before starting the seatbelt detection
time.sleep(5)

# Loop over the frames from the video stream
while True:
    # Read a frame from the video stream
    ret, frame = cap.read()
    assert ret, "Error: Could not read frame from video stream"

    # Convert the frame to RGB format
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Run the hand detection model on the image and retrieve the hand landmarks
    results = hands.process(image)
    landmarks = results.multi_hand_landmarks

    # Extract the hand landmarks' position and orientation and determine if they are on the steering wheel
    if landmarks:
        for hand_landmarks in landmarks:
            # Get the coordinates of the relevant landmarks
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            middle_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
            ring_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
            little_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

            # Check if the hand is on the steering wheel
            # You can adjust the threshold values based on the size of the steering wheel in the image
            if (
                thumb_tip.y < index_finger_tip.y
                and middle_finger_tip.y < ring_finger_tip.y
                and ring_finger_tip.y < little_finger_tip.y
                and thumb_tip.x < index_finger_tip.x
                and thumb_tip.x < middle_finger_tip.x
                and thumb_tip.x < ring_finger_tip.x
                and thumb_tip.x < little_finger_tip.x
                and thumb_tip.x < 0.4 * image.shape[1]
            ):
                # Hands on the steering wheel
                cv2.putText(frame, "Hands on the steering wheel", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            else:
                # Hands not on the steering wheel
                cv2.putText(frame, "Hands off the steering wheel", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                # Play the alert sound in a separate thread
                t = Thread(target=play_alert_sound)
                t.daemon = True
                t.start()

    # Display the frame in the window
    cv2.imshow("Hands on the Steering Wheel Detection", frame)

    # Check if the 'q' key was pressed to quit the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close the OpenCV window
cap.release()
cv2.destroyAllWindows()

