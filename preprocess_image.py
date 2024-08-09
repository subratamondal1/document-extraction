import cv2
import numpy as np
from PIL import Image
import io

def grayscale_contrast(uploaded_image):
    """Returns a PIL Image object of the preprocessed image"""
    # Read the image from the uploaded file-like object
    file_bytes = np.asarray(bytearray(uploaded_image.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    # Check if the image was loaded successfully
    if image is None:
        raise ValueError(
            "Error: Unable to read the image. Please upload a valid image file."
        )

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply bilateral filter to reduce noise while preserving edges
    filtered = cv2.bilateralFilter(gray, d=9, sigmaColor=75, sigmaSpace=75)

    # Apply adaptive thresholding
    adaptive_thresh = cv2.adaptiveThreshold(
        filtered, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
    )

    # Optional: Morphological operations to enhance text
    kernel = np.ones((3, 3), np.uint8)
    morph = cv2.morphologyEx(adaptive_thresh, cv2.MORPH_CLOSE, kernel)

    # Convert the preprocessed image to a PIL Image object
    pil_image = Image.fromarray(morph)

    return pil_image