import cv2
import os
import random
IMAGE_DIR = "Dataset/images/train"
LABEL_DIR = "Dataset/labels/train"

image_files = [
    f for f in os.listdir(IMAGE_DIR)
    if f.endswith((".jpg", ".jpeg", ".png"))
]

image_name = random.choice(image_files)

image_path = os.path.join(IMAGE_DIR, image_name)
label_path = os.path.join(
    LABEL_DIR,
    os.path.splitext(image_name)[0] + ".txt"
)

image = cv2.imread(image_path)

height, width = image.shape[:2]

with open(label_path, "r") as f:
    lines = f.readlines()

for line in lines:

    cls, x, y, w, h = map(float, line.split())

    x1 = int((x - w/2) * width)
    y1 = int((y - h/2) * height)

    x2 = int((x + w/2) * width)
    y2 = int((y + h/2) * height)

    color = (0,255,0) if int(cls)==0 else (0,0,255)

    label = "Crop" if int(cls)==0 else "Weed"

    cv2.rectangle(image,(x1,y1),(x2,y2),color,2)

    cv2.putText(image,
                label,
                (x1,y1-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                color,
                2)

cv2.imshow("Dataset Visualization", image)

cv2.waitKey(0)
cv2.destroyAllWindows()