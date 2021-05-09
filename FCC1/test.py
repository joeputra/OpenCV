import cv2
from google.colab.patches import cv2_imshow

# colorful image - 3 channels
image = cv2.imread("opencvTutorial/images/color.jpg")
print(image.shape)
