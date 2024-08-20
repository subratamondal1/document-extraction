import cv2
import numpy as np
from PIL import Image


def detect_tables_in_handwritten_image(pil_image):
    """Detects only the largest table in a handwritten text image, creates a bounding box around it, and returns the cropped area."""

    # Convert the PIL Image to an OpenCV image format
    image = np.array(pil_image.convert('RGB'))  # Convert to RGB if not already
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # Convert to BGR for OpenCV

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply adaptive thresholding to detect structures
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY_INV, 11, 2)

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL,
                                   cv2.CHAIN_APPROX_SIMPLE)

    largest_area = 0
    largest_contour = None

    # Iterate over contours to find the largest table based on area
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        area = w * h

        # Update largest area and contour if this one is larger
        if area > largest_area:
            largest_area = area
            largest_contour = (x, y, w, h)

    cropped_image = None
    if largest_contour is not None:
        x, y, w, h = largest_contour
        # Draw bounding box around detected largest table
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        # Crop the image within the bounding box
        cropped = image[y:y + h, x:x + w]
        # Convert the cropped image back to PIL format
        cropped_image = Image.fromarray(
            cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB))

    # Convert the original image with bounding boxes back to PIL format
    result_pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    return result_pil_image, cropped_image
