from ultralytics import YOLO
import os
model = YOLO("yolov8n.pt")
print("Current directory:", os.getcwd())
print("Dataset exists:", os.path.exists("Dataset"))
print("Train exists:", os.path.exists("Dataset/images/train"))
print("Labels exists:", os.path.exists("Dataset/labels/train"))
model.train(
    data="Dataset/data.yaml",
    epochs=50,
    imgsz=512,
    batch=8,          
    workers=2,       
    device="cpu",     
    cache=False,      
    project="Results",
    name="Crop_Weed_Detection"
)