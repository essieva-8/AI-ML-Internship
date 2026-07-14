# Task 2

print("LabelImg : Open-source annotation tool.\nBeginner-friendly interface.\nUsed for drawing bounding boxes.\nSaves annotations in YOLO, Pascal VOC, and other formats.\nSuitable for small and medium-sized datasets.")

print("Roboflow : Cloud-based annotation platform.\nSupports annotation, dataset management, augmentation, and exporting.\nCan export directly in YOLO format.\nWidely used for computer vision projects.\nExcellent for collaborative work.")

print("CVAT : Advanced annotation tool developed for large-scale datasets.\nSupports image and video annotation.\nProvides automatic annotation features using AI.\nSuitable for professional and enterprise-level projects.")


#Task 3

print("\n========== Dataset Structure ==========\n")

dataset_structure = """
dataset/
│
├── images/
│   ├── train/
│   │     helmet1.jpg
│   │     helmet2.jpg
│   │
│   └── val/
│         helmet3.jpg
│
└── labels/
    ├── train/
    │     helmet1.txt
    │     helmet2.txt
    │
    └── val/
          helmet3.txt
"""

print(dataset_structure)


#Task 4

print("\n========== data.yaml ==========\n")

data_yaml = """
train: dataset/images/train
val: dataset/images/val

nc: 1

names:
  - helmet
"""

print(data_yaml)


#Task 5

from ultralytics import YOLO

# Load the pre-trained YOLOv8 model
model = YOLO("yolov8n.pt")

# Train the model on the custom dataset
model.train(
    data="data.yaml",
    epochs=10
)



