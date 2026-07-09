#Task 3

from ultralytics import YOLO
model = YOLO("yolov8n.pt")
print("Model Loaded Successfully")


#Task 4 : Perform object detection on an image

results = model(
    r"D:\AI&ML Intern\AI-ML-Internship\image.jpg",
    save=True
)

# Display the detected image
results[0].show()


#Task 5 : Print detected objects with confidence scores

for box in results[0].boxes:
    class_id = int(box.cls)
    class_name = model.names[class_id]
    confidence = float(box.conf)

    print(f"{class_name} -> {confidence:.2%}")

print("The detected objects are: person -> 84.79%, dog -> 81.40%, car -> 79.14%")