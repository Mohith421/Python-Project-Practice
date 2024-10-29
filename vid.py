import os
import numpy as np
import cv2

def cartoonize_image(img):
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply median blur to smooth the image
    gray = cv2.medianBlur(gray, 5)
    
    # Detect edges in the image
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    
    # Create a color image
    color = cv2.bilateralFilter(img, 9, 300, 300)
    
    # Combine the edges and color images to get the cartoon effect
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    
    return cartoon

# Prompt the user to enter the image file path
image_path = input("Enter the path of the image you want to cartoonize: ")

# Read the image
img = cv2.imread(image_path)

if img is None:
    print("Error: Unable to read image file")
    exit(1)

# Apply cartoonize effect
cartoon_image = cartoonize_image(img)

# Display the original and cartoonized images
cv2.imshow("Original Image", img)
cv2.imshow("Cartoonized Image", cartoon_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the cartoonized image
output_folder = "cartoonized_images"
os.makedirs(output_folder, exist_ok=True)
output_path = os.path.join(output_folder, "cartoonized_" + os.path.basename(image_path))
cv2.imwrite(output_path, cartoon_image)
print("Cartoonized image saved at:", output_path)
