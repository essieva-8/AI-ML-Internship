#Task 1

from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# Run object detection
results = model(r"D:\\AI&ML Intern\\AI-ML-Internship\\image.jpg", save=True)
# Display the detected image
results[0].show()
print("Object detection completed.")


#Task 2

print("Detected Objects and Confidence Scores")

for result in results:
    for box in result.boxes:
        class_id = int(box.cls[0])
        class_name = result.names[class_id]
        confidence = float(box.conf[0])

        print(f"{class_name} -> {confidence:.2%}")


#Task 3

confidence_values = [0.3, 0.5, 0.8]

for conf in confidence_values:
    print("Confidence Threshold =", conf)
    results = model.predict(r"D:\\AI&ML Intern\\AI-ML-Internship\\image.jpg", conf=conf)
    results[0].show()
print("\nObservation:")
print("Lower confidence thresholds detect more objects, including uncertain ones.")
print("Higher confidence thresholds display only highly confident detections.")


#Task 4

results = model.predict(r"D:\\AI&ML Intern\\AI-ML-Internship\\image.jpg", conf=0.5)
for result in results:
    print(result.boxes)

print("\nAnalysis:")
print("The output contains bounding box coordinates, confidence scores, and class IDs for each detected object.")


#Task 5

results = model.predict(r"D:\\AI&ML Intern\\AI-ML-Internship\\image.jpg", conf=0.5)
for result in results:
    for box in result.boxes:
        class_id = int(box.cls[0])
        class_name = result.names[class_id]
        confidence = float(box.conf[0])
        bbox = box.xyxy[0].tolist()

        print("Object Class :", class_name)
        print("Confidence :", confidence)
        print("Bounding Box :", bbox)
        print()           