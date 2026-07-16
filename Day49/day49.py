#Task 1

from ultralytics import YOLO
model = YOLO("yolov8n.pt")

# Train the model
model.train(
    data="data.yaml",      
    epochs=10,
    imgsz=640,
    batch=8,
    project="runs",
    name="helmet_detection"
)


#Task 2

print("""
runs/
└── detect/
    └── train/
        ├── best.pt
        ├── last.pt
        └── results.png
""")


#Task 3

print("Ideal Training Graph Analysis:")

print("""
Loss       -> Should decrease.
Precision  -> Should increase.
Recall     -> Should increase.
mAP        -> Should increase.
""")


#Task 4

print("Training Metrics Comparison:")

print("""
| Metric            | Epoch 1 | Epoch 10 |
| ----------------- | ------- | -------- |
| Loss              | High    | Lower    |
| Precision         | Low     | Higher   |
| Recall            | Low     | Higher   |
| mAP               | Low     | Higher   |
| Detection Quality | Poor    | Better   |
""")


#Task 5 

print("Explanation of Loss Decrease:")
print("Loss decreases because, during each epoch, the YOLO model compares its predictions with the actual labels and updates its internal weights using the optimization algorithm (backpropagation and gradient descent). These updates reduce prediction errors over time, allowing the model to make more accurate object detections. As learning improves, the loss gradually decreases while precision, recall, and mAP increase.")