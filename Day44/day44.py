#Task 1 : Install YOLO

# pip install ultralytics


#Task 2 : Import YOLO

from ultralytics import YOLO


#Task 3 : Load YOLOv8 Model

model = YOLO("yolov8n.pt")
print("YOLOv8 model loaded successfully!")


#Task 4 : Research on YOLO Versions

yolo_versions = {
    "YOLOv3": "Introduced Darknet-53 backbone and improved detection accuracy.",
    "YOLOv5": "Popular version developed by Ultralytics, easy to train and deploy.",
    "YOLOv8": "Latest Ultralytics version with improved speed, accuracy, and usability."
}

print("\nYOLO Version Research:")
for version, description in yolo_versions.items():
    print(f"{version}: {description}")


#Task 5 : 10 Real-World Applications of YOLO

applications = [
    "1. Self-Driving Cars",
    "2. Face Detection and Recognition",
    "3. CCTV Surveillance",
    "4. Traffic Monitoring",
    "5. Medical Image Analysis",
    "6. Retail Product Detection",
    "7. Intruder Detection Systems",
    "8. Industrial Defect Detection",
    "9. Wildlife Monitoring",
    "10. Robotics and Automation"
]

print("\n10 Real-World Applications of YOLO:")
for app in applications:
    print(app)


