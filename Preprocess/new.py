from ultralytics import YOLO

model = YOLO("Results/Crop_Weed_Detection-16/weights/best.pt")

metrics = model.val(data="Dataset/data.yaml")

print(metrics)