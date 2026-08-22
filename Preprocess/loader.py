import os

# Change this path to your dataset folder
DATASET_PATH = "Dataset/raw"
image_extensions = (".jpg", ".jpeg", ".png")

images = []
labels = []

for file in os.listdir(DATASET_PATH):
    if file.lower().endswith(image_extensions):
        images.append(os.path.splitext(file)[0])

    elif file.lower().endswith(".txt"):
        labels.append(os.path.splitext(file)[0])

print(f"Total Images : {len(images)}")
print(f"Total Labels : {len(labels)}")

missing_labels = []

for image in images:
    if image not in labels:
        missing_labels.append(image)

print(f"Images without labels : {len(missing_labels)}")

if len(missing_labels) == 0:
    print("✅ Every image has a corresponding label.")
else:
    print("Missing labels:")
    print(missing_labels[:10])