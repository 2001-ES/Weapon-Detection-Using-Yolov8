# Weapon-Detection-Using-Yolov8

A real-time object detection system to identify and localize dangerous weapons such as guns, knives, grenades, and blades using the YOLOv8 deep learning model. This project is designed to enhance security through AI-based threat detection in public places like airports, schools, and malls.

📁 Dataset
The dataset used for training this model was sourced from Roboflow. It includes labeled images of various weapons such as:

Guns
Knives
Blades
Grenades

All images were annotated in YOLO format and preprocessed to ensure compatibility with the Ultralytics YOLOv8 model.

🧠 Model
We used the YOLOv8 (You Only Look Once Version 8) architecture for object detection, provided by Ultralytics.The model was trained on the Roboflow dataset and the best-performing weights were saved as best.pt
Use of best.pt:
best.pt contains the trained model weights after optimizing on the dataset.
It can be used for inference to detect weapons in images or real-time video streams.
Load it using Ultralytics YOLOv8 for accurate weapon detection.



