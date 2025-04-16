# test_deepface.py

from deepface import DeepFace
from PIL import Image
import numpy as np

# Use your test image path
img_path = "test.jpg"  # Replace this with the path to your image

img = Image.open(img_path)
img_array = np.array(img)

result = DeepFace.analyze(
    img_array,
    actions=["age", "emotion"],
    enforce_detection=False
)

print("✅ DeepFace Output:")
print(result)

