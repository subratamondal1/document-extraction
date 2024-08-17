import cv2
import numpy as np
from PIL import Image

def detect_tables_in_handwritten_image(pil_image):
    """Detects tables in a handwritten text image, creates bounding boxes around them, and crops the detected areas."""

    # Convert the PIL Image to an OpenCV image format
    image = np.array(pil_image.convert('RGB'))  # Convert to RGB if not already
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # Convert to BGR for OpenCV

    # Convert the image to grayscale (if not already done in preprocessing)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply adaptive thresholding to detect structures
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY_INV, 11, 2)

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL,
                                   cv2.CHAIN_APPROX_SIMPLE)

    cropped_images = []  # List to store cropped images

    # Iterate over contours to detect tables based on aspect ratio and area
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)

        # Filter out small or irregular contours that are unlikely to be tables
        aspect_ratio = w / float(h)
        area = w * h

        if 0.5 < aspect_ratio < 2.5 and area > 1000:  # Adjust thresholds based on your images
            # Draw bounding box around detected table
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

            # Crop the image within the bounding box
            cropped = image[y:y+h, x:x+w]

            # Convert the cropped image back to PIL format
            cropped_pil_image = Image.fromarray(cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB))

            # Append cropped image to the list
            cropped_images.append(cropped_pil_image)

    # Convert the original image with bounding boxes back to PIL format
    result_pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    return result_pil_image, cropped_images