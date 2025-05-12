from ultralytics import YOLO

model = YOLO(r'C:\Users\Dell\Desktop\Weapon detection\best.pt')
# Run webcam prediction
model.predict(source='0', imgsz=640, conf=0.6, save=True, show=True)
