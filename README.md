ntelliCane

An AI-powered smart cane designed to empower visually impaired individuals with enhanced situational awareness.
🏆 Winner of Best Accessibility Hack at MakeUofT 2023

📖 Overview
IntelliCane is an innovative assistive device that combines IoT and AI technologies to improve mobility and safety for visually impaired users. Equipped with sensors, a camera, and advanced object detection capabilities, IntelliCane provides real-time feedback to help users navigate their environment confidently.

💡 Features

Obstacle Detection: Ultrasonic sensor detects objects within a 2-meter range and triggers alerts via a piezo buzzer.

Real-Time Object Recognition: Integrates a YOLOv8 model and a custom-trained CNN for precise identification of objects in the user’s path.

Audio Feedback: Delivers intuitive voice prompts via a portable speaker, enhancing situational awareness.

Compact and Portable Design: Built with Arduino and Raspberry Pi for lightweight, reliable operation.

🛠️ Technology Stack

Hardware: Arduino UNO, Raspberry Pi, Ultrasonic Sensor, Piezo Buzzer, Camera Module

Programming Languages: Python, C++

AI/ML Frameworks: YOLOv8, Custom CNN Model

Additional Tools: OpenCV, TensorFlow

📋 Architecture

Obstacle Detection Module:

Ultrasonic sensor monitors the user's immediate surroundings.

Signals are processed by the Arduino, which activates the piezo buzzer to alert the user.

Object Recognition Module:

Raspberry Pi captures real-time video streams.

YOLOv8 and custom CNN identify objects and provide classification data.

Feedback System:

Portable speaker communicates navigation instructions based on detected obstacles and objects.
