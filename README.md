# AI Driver Safety System 🚗💡

Welcome to the AI Driver Safety System, an open-source initiative harnessing the power of computer vision and machine learning to revolutionize road safety.

# Key Features
Animal detection
In this project we aim to protect driver from animals that face him at the road by alerting him .
we use yolo v8 on our custom data to detect animals
Animal_detection.pt this is our model you can use it in your data
Animal_detection.py this is areal time animal detection Image 1 Image 2

- #### Vigilant Monitoring:
  Utilizes machine learning for head and body detection to ensure driver attentiveness.
  ![Image](https://github.com/rania-hossam/AI_Driver_safety_System-/blob/main/gifs/drowness.mp4)

- #### Road Awareness:
  Implements Hough transform for precise line detection and robust stop sign recognition.
  ![Image](https://github.com/rania-hossam/AI_Driver_safety_System-/blob/main/gifs/road_awarness.mp4)

- ### Posture Correction:
focusing on the detection and analysis of a driver's behavior. It employs MediaPipe's holistic model for detecting facial landmarks, hand positions, and body posture. The script includes functions to check if the driver is looking at the road, holding the steering wheel correctly, and maintaining proper posture. Visual feedback is provided in real-time by drawing landmarks on the video feed and overlaying text messages indicating the driver's state (e.g., looking at the road, holding the steering wheel properly). The script runs continuously until 'q' is pressed to exit  ![Image](https://github.com/rania-hossam/AI_Driver_safety_System-/blob/main/gifs/drowness.mp4)

- ### Seatbelt Adherence:
monitoring a driver's hand position on the steering wheel. The alert system, which is triggered when the hands are not detected on the wheel, demonstrates a practical use case in driver safety systems.![Image](https://github.com/rania-hossam/AI_Driver_safety_System-/blob/main/gifs/seatbelt.mp4)

- ### Proximity Sensing:
  Integrates ToF sensors to alert drivers about the proximity of objects , the sensors will be installed in multiple points in the car
  allowing them to almost sense for any object coming close to the car , and alerting the driver in various ways allowing him to do stuff like parking more effectively ,
  also using it's readings in various calculations enhancing the overall driving safty .
# Hardware Setup
- ### Raspberry Pi 4:
  The brain of our system, providing a powerful yet compact computing platform.
- ### VLX ToF Sensors: 
  Our eyes for distance measuring, ensuring a safer driving environment.
- ### Pi Camera:
  Captures real-time footage for our detection algorithms to analyze.
# Prototype Demonstration 
we made a simple 3d desgin for a sesnor head with 5 vlx sensors that measures and looks for obstacles from different angels, 
this prototype can be installed on a mini car showing how these sensors can work with the models , this can be enhanced even more later for more precise measurements of various other factors ,
here is how or 3d printed sensor head looks :

![photo_2024-01-04_18-36-51](https://github.com/rania-hossam/AI_Driver_safety_System-/assets/103861444/a2579d22-bce6-489a-8f3b-249e8293ddd6)

![photo_2024-01-04_18-36-48](https://github.com/rania-hossam/AI_Driver_safety_System-/assets/103861444/364560ce-a04d-4409-a4fe-1b30837a6021)




# Get Involved
Check out our installation guide and follow the simple steps to set up the system on your Raspberry Pi 4.
