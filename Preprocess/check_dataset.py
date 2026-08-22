import os
from PIL import Image

image_dir = "Dataset/Images/train"
label_dir = "Dataset/labels/train"

count = 0

for image_file in os.listdir(image_dir):
    if not image_file.lower().endswith((".jpg", ".jpeg", ".png")):
        continue

    label_file = os.path.splitext(image_file)[0] + ".txt"
    label_path = os.path.join(label_dir, label_file)

    if not os.path.exists(label_path):
        print(f"Missing label: {label_file}")
        continue

    img = Image.open(os.path.join(image_dir, image_file))
    w, h = img.size

    with open(label_path) as f:
        lines = f.readlines()

    if len(lines) == 0:
        print(f"Empty label: {label_file}")
        continue

    for line in lines:
        parts = line.strip().split()

        if len(parts) != 5:
            print(f"Invalid format: {label_file} -> {line}")
            continue

        cls, x, y, bw, bh = map(float, parts)

        if not (0 <= cls <= 1):
            print(f"Invalid class: {label_file}")

        if not (0 <= x <= 1 and 0 <= y <= 1 and 0 < bw <= 1 and 0 < bh <= 1):
            print(f"Invalid coordinates: {label_file}")

    count += 1

print(f"Checked {count} files.")