from PIL import Image
from utils.face_utils import predict_with_child_model

img_path = "test.jpg"  # Make sure the image exists here
img = Image.open(img_path)
age_group = predict_with_child_model(img)
print("Predicted Age Group:", age_group)
