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

    # Apply histogram equalization to increase contrast
    equalized = cv2.equalizeHist(gray)

    # Apply sharpening filter
    kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    sharpened = cv2.filter2D(equalized, -1, kernel)

    # Convert the preprocessed image to a PIL Image object
    pil_image = Image.fromarray(sharpened)

    return pil_image
