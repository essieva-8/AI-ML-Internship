#Task 1

from ultralytics import YOLO
model = YOLO("yolov8n.pt")

# Train the model on the custom helmet dataset
model.train(
    data=r"d:\AI&ML Intern\AI-ML-Internship\Day49\HelmetDataset\data.yaml",
    epochs=10,
    imgsz=640
)

print("\nObservations:")
print("1. The YOLOv8 Nano model was successfully trained on the custom helmet detection dataset.")
print("2. Training completed for 10 epochs.")
print("3. The final Box Loss was 2.157.")
print("4. The final Classification Loss was 2.572.")
print("5. The final DFL Loss was 1.414.")
print("6. The model achieved a Precision of 0.00667.")
print("7. The Recall obtained was 0.222.")
print("8. The mAP@50 was 0.0596.")
print("9. The mAP@50-95 was 0.0355.")
print("10. The low Precision, Recall, and mAP values indicate that the model's detection performance is limited due to the very small training dataset (approximately 10 images).")
print("11. Increasing the number of annotated images and training for more epochs would improve the model's performance.")


#Task 2

print("\nGenerated Files:")
print("-" * 50)
print(f"{'File':<15} {'Location'}")
print("-" * 50)
print(f"{'best.pt':<15} runs/detect/train-6/weights/")
print(f"{'last.pt':<15} runs/detect/train-6/weights/")
print(f"{'results.png':<15} runs/detect/train-6/")
print("-" * 50)


#Task 3

print("\nTraining Graph Analysis:")
print("1. The Box Loss curve shows an increasing trend, indicating that the model's bounding box localization did not improve.")
print("2. The Classification Loss curve shows a decreasing trend, indicating improved classification performance during training.")
print("3. The DFL Loss curve shows an increasing trend, suggesting that the bounding box coordinate predictions became less accurate.")
print("4. The Precision curve shows a decreasing trend, indicating a reduction in the accuracy of positive detections.")
print("5. The Recall curve shows a decreasing trend, indicating that the model detected fewer actual helmet instances.")
print("6. The Validation mAP curve shows an increasing trend, indicating a slight improvement in overall detection performance on the validation dataset.")
print("7. Overall, the model learned only to a limited extent because it was trained on a very small dataset.")


#Task 4

print("\nEpoch 1 vs Epoch 10 Analysis:")
print("1. Box Loss increased from 1.770 to 2.157, indicating reduced bounding box localization accuracy.")
print("2. Classification Loss decreased from 3.550 to 2.572, showing improved classification performance.")
print("3. DFL Loss increased slightly from 1.334 to 1.414, indicating a slight reduction in localization accuracy.")
print("4. Precision decreased from 0.020 to 0.00667, indicating more false positive predictions.")
print("5. Recall decreased from 0.667 to 0.222, indicating fewer helmet instances were detected.")
print("6. mAP@50 increased from 0.0177 to 0.0596, showing improved overall detection accuracy.")
print("7. mAP@50-95 increased from 0.00906 to 0.0355, indicating an improvement in overall model performance.")
print("8. Although mAP improved, the overall performance remained low because the model was trained on a very small dataset.")


#Task 5 

print("Explanation of Loss Decrease:")
print("Loss decreases because, during each epoch, the YOLO model compares its predictions with the actual labels and updates its internal weights using the optimization algorithm (backpropagation and gradient descent). These updates reduce prediction errors over time, allowing the model to make more accurate object detections. As learning improves, the loss gradually decreases while precision, recall, and mAP increase.")