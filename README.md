# AI Driver Safety System 🚗💡

Welcome to the AI Driver Safety System, a cutting-edge open-source project designed to enhance road safety through advanced computer vision and machine learning technologies. Our system focuses on preventing accidents and ensuring driver vigilance, utilizing state-of-the-art algorithms and hardware integration.

## Key Features

### 🐾 Animal Detection
To safeguard drivers from potential animal-related accidents, our system employs the latest YOLO v8 algorithm on custom datasets. 
- **Model**: `Animal_detection.pt` - Deploy our pre-trained model for immediate use.
- **Script**: `Animal_detection.py` - Experience real-time animal detection.
- **Visuals**: See our system in action with sample images and videos.

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
