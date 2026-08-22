import os
import random
import shutil

# Paths
RAW_DATASET = "dataset/agri_data/data"

IMAGE_DEST = "Dataset/images"
LABEL_DEST = "Dataset/labels"

# Create destination folders
for folder in ["train", "val", "test"]:
    os.makedirs(os.path.join(IMAGE_DEST, folder), exist_ok=True)
    os.makedirs(os.path.join(LABEL_DEST, folder), exist_ok=True)

# Image extensions
image_extensions = (".jpg", ".jpeg", ".png")

# Get all images
images = [
    f for f in os.listdir(RAW_DATASET)
    if f.lower().endswith(image_extensions)
]

# Shuffle dataset
random.seed(42)
random.shuffle(images)

# Split sizes
total = len(images)

train_end = int(0.7 * total)
val_end = int(0.9 * total)

train = images[:train_end]
val = images[train_end:val_end]
test = images[val_end:]

dataset = {
    "train": train,
    "val": val,
    "test": test
}

# Copy images and labels
for split, files in dataset.items():

    for image in files:

        image_src = os.path.join(RAW_DATASET, image)

        label = os.path.splitext(image)[0] + ".txt"
        label_src = os.path.join(RAW_DATASET, label)

        shutil.copy(image_src,
                    os.path.join(IMAGE_DEST, split, image))

        shutil.copy(label_src,
                    os.path.join(LABEL_DEST, split, label))

print("Dataset Split Completed Successfully!\n")

print(f"Train Images : {len(train)}")
print(f"Validation Images : {len(val)}")
print(f"Test Images : {len(test)}")