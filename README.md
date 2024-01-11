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
  ![Image](https://github.com/rania-hossam/AI_Driver_safety_System-/blob/main/AI_DRIVER_SYSTEM/object_tracking_usingyoloV8/track_all_seg_1280_025conf.gif)
  ![Image](https://github.com/rania-hossam/AI_Driver_safety_System-/blob/main/gifs/VID-20240109-WA0013.mp4)

- #### Road Awareness:
- emonstrates how to detect straight lines in an image using the Hough Transform in OpenCV. It reads an image, processes it to detect edges, and then applies the Hough Line Transform to find and draw lines on the original image.
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




# AI Driver Safety System 🚗💡

Welcome to the AI Driver Safety System, a cutting-edge open-source project designed to enhance road safety through advanced computer vision and machine learning technologies. Our system focuses on preventing accidents and ensuring driver vigilance, utilizing state-of-the-art algorithms and hardware integration.

## Key Features

### 🐾 Animal Detection
To safeguard drivers from potential animal-related accidents, our system employs the latest YOLO v8 algorithm on custom datasets. 
- **Model**: `Animal_detection.pt` - Deploy our pre-trained model for immediate use.
- **Script**: `Animal_detection.py` - Experience real-time animal detection.
- **Visuals**: See our system in action with sample images and videos.

- Crack detection
In this project we aim to protect driver from crack in the by alerting him .
we use yolo v8 on our custom data to detect crack at the road
Crack_detection.pt this is our model you can use it in your data
Crack_detection.py this is areal time Crack detection Image 1 Image 2


### 🔍 Vigilant Monitoring
Our system uses sophisticated machine learning algorithms for real-time head and body detection, ensuring driver attentiveness at all times.
- **Demo**: [Watch how our system detects drowsiness](https://github.com/rania-hossam/AI_Driver_safety_System-/blob/main/gifs/drowness.mp4).

### 🚧 Road Awareness
This feature demonstrates the use of the Hough Transform in OpenCV to detect and visualize straight lines, crucial for road lane detection.
- **Demo**: [See Road Awareness in action](https://github.com/rania-hossam/AI_Driver_safety_System-/blob/main/gifs/road_awarness.mp4).

### 🧍‍♂️ Posture Correction
Employing MediaPipe's holistic model, our system analyzes the driver's posture, facial landmarks, and hand positions, ensuring that they are focused on the road and holding the steering wheel correctly.
- **Feedback**: Real-time visual feedback is provided to alert the driver.
- **Demo**: [Observe Posture Correction in action](https://github.com/rania-hossam/AI_Driver_safety_System-/blob/main/gifs/drowness.mp4).

### 🔒 Seatbelt Adherence
Our monitoring system also focuses on the driver’s hand position on the steering wheel, alerting if the hands are not detected, thereby enhancing safety.
- **Demo**: [View Seatbelt Adherence demonstration](https://github.com/rania-hossam/AI_Driver_safety_System-/blob/main/gifs/seatbelt.mp4).

### 📏 Proximity Sensing
Integrating ToF sensors, our system alerts drivers about the proximity of objects, aiding in efficient parking and enhancing overall safety.
- **Application**: Utilized for effective parking assistance and collision avoidance.

## Hardware Setup

### 🧠 Raspberry Pi 4
The core computing platform, providing robust and compact processing capabilities.

### 👁️ VLX ToF Sensors
Our advanced distance measuring sensors, crucial for a safe driving environment.

### 📷 Pi Camera
Captures real-time footage for analysis by our detection algorithms.

## Prototype Demonstration 
We've developed a 3D-designed sensor head equipped with 5 VLX sensors, capable of detecting obstacles from various angles. This prototype demonstrates the practical application of our sensors in real-world scenarios.
- **3D Prototype**: Check out our innovative sensor head design.

![Sensor Head Prototype](https://github.com/rania-hossam/AI_Driver_safety_System-/assets/103861444/a2579d22-bce6-489a-8f3b-249e8293ddd6)

![Sensor Head Prototype 2](https://github.com/rania-hossam/AI_Driver_safety_System-/assets/103861444/364560ce-a04d-4409-a4fe-1b30837a6021)

## Get Involved
Join us in revolutionizing driver safety. Follow our comprehensive installation guide to set up the system on your Raspberry Pi 4 and contribute to a safer driving future.

---

This enhanced README provides a more professional, clear, and engaging description of the AI Driver Safety System. It outlines the system's features, hardware setup, and involvement opportunities, making it an excellent resource for users and contributors.
