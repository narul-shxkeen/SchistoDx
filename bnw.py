import os
import cv2
import numpy as np
from pathlib import Path

img_path = "./2024-03-12_01-34-30-081406.jpg"
output_dir = Path("./")

# Read the image first
img = cv2.imread(img_path)

# Convert to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Save to output directory
img_filename = Path(img_path).name
output_path = output_dir / img_filename
cv2.imwrite(str(output_path), gray_img)