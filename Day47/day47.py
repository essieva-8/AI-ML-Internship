#Task 2

from ultralytics import YOLO

# Load YOLOv8 Nano Model
model = YOLO("yolov8n.pt")

print("YOLO Model Loaded Successfully")


#Task 3 - Run detection on a video file

import cv2
from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolov8n.pt")

# Read video
video = cv2.VideoCapture(r"D:\AI&ML Intern\AI-ML-Internship\video.mp4")

while True:
    success, frame = video.read()

    if not success:
        break

    # Detect objects
    results = model(frame, save =True)

    for result in results:
        for box in result.boxes:
            class_name = model.names[int(box.cls[0])]
            confidence = float(box.conf[0])

            print(f"{class_name}: {confidence:.2f}")


    # Draw bounding boxes
    annotated_frame = results[0].plot()

    # Display output
    cv2.imshow("YOLO Video Detection", annotated_frame)

    # Press ESC to exit
    if cv2.waitKey(1) == 27:
        break

video.release()
cv2.destroyAllWindows()


#Task 4 - Run real-time webcam detection

# Open webcam
camera = cv2.VideoCapture(0)

while True:
    success, frame = camera.read()

    if not success:
        break

    # Detect objects
    results = model(frame)

    for result in results:
        for box in result.boxes:
            class_name = model.names[int(box.cls[0])]
            confidence = float(box.conf[0])

            print(f"{class_name}: {confidence:.2f}")

    # Draw bounding boxes
    annotated_frame = results[0].plot()

    # Display output
    cv2.imshow("Live Object Detection", annotated_frame)

    # Press ESC to exit
    if cv2.waitKey(1) == 27:
        break

camera.release()
cv2.destroyAllWindows()


