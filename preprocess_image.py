import cv2
import numpy as np
from PIL import Image, ImageEnhance
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
    adaptive_thresh = cv2.adaptiveThreshold(filtered, 255,
                                            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                            cv2.THRESH_BINARY, 11, 2)

    # Optional: Morphological operations to enhance text
    kernel = np.ones((3, 3), np.uint8)
    morph = cv2.morphologyEx(adaptive_thresh, cv2.MORPH_CLOSE, kernel)

    # Convert the preprocessed image to a PIL Image object
    pil_image = Image.fromarray(morph)

    return pil_image


def adobe_like_preprocessing(uploaded_image):
    """Applies preprocessing to enhance text visibility while minimizing bleed-through."""
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

    # Apply Gaussian blur with a smaller kernel to reduce bleed-through but preserve text
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)

    # Apply adaptive thresholding with slightly stricter settings to retain text clarity
    adaptive_thresh = cv2.adaptiveThreshold(blurred, 255,
                                            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                            cv2.THRESH_BINARY, 25, 8)

    # Apply a morphological operation to clean up small dots and noise
    kernel = np.ones((2, 2), np.uint8)
    cleaned = cv2.morphologyEx(adaptive_thresh, cv2.MORPH_OPEN, kernel)

    # Convert the preprocessed image to a PIL Image object
    pil_image = Image.fromarray(cleaned)

    return pil_image


def enhance_color_contrast(uploaded_image):
    """Enhances color and contrast to make text more visible and reduce bleed-through, then converts to black and white."""
    # Read the image from the uploaded file-like object
    file_bytes = np.asarray(bytearray(uploaded_image.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    # Check if the image was loaded successfully
    if image is None:
        raise ValueError(
            "Error: Unable to read the image. Please upload a valid image file."
        )

    # Convert the image to PIL for easy manipulation
    pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # Enhance the contrast
    contrast_enhancer = ImageEnhance.Contrast(pil_image)
    pil_image = contrast_enhancer.enhance(
        1.5)  # Increase contrast (adjust the factor as needed)

    # Enhance the color saturation
    color_enhancer = ImageEnhance.Color(pil_image)
    pil_image = color_enhancer.enhance(
        1.5)  # Increase saturation (adjust the factor as needed)

    # Convert back to OpenCV format
    enhanced_image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

    # Optional: Apply mild denoising to reduce any remaining noise
    denoised_image = cv2.fastNlMeansDenoisingColored(enhanced_image, None, 10,
                                                     10, 7, 21)

    # Convert the denoised image back to a PIL Image object for final processing
    final_pil_image = Image.fromarray(denoised_image)

    # Convert the image to grayscale
    grayscale_image = final_pil_image.convert('L')

    # Adjust the brightness of the grayscale image
    brightness_enhancer = ImageEnhance.Brightness(grayscale_image)
    brightened_image = brightness_enhancer.enhance(1.2)

    return brightened_image
