#Task 2 - Design dataset structure

print(""" 
helmet_dataset/
│
├── images/
│   ├── train/
│   └── val/
│
└── labels/
    ├── train/
    └── val/)
""")


#Task 3 - Write a sample data.yaml

print(""" 
train: helmet_dataset/images/train
val: helmet_dataset/images/val

nc: 1

names:
  - helmet
""")


#Task 4 - Write YOLO training code

from ultralytics import YOLO

# Load YOLOv8 Nano Model
model = YOLO("yolov8n.pt")

# Train the model
model.train(
    data="data.yaml",
    epochs=20
)

print("Training Completed Successfully!")

# Load trained model
model = YOLO("runs/detect/train/weights/best.pt")

# Test image
results = model("test_image.jpg")

# Display result
results[0].show()

print("Testing Completed Successfully!")
import cv2 
from ultralytics import YOLO 
model = YOLO( "runs/detect/train/weights/best.pt" ) 
cap = cv2.VideoCapture(0) 
while True: 
    success, frame = cap.read() 
    if not success: 
        break 
    results = model(frame) 
    annotated_frame = results[0].plot() 
    cv2.imshow( "Helmet Detection", annotated_frame ) 
    if cv2.waitKey(1) == 27: 
        break 
cap.release() 
cv2.destroyAllWindows()



