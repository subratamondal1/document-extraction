<center><h1>Document Extraction</h1></center>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.10.14-yellow" alt="python@3.10.14">
  <img src="https://img.shields.io/badge/numpy-2.0.1-moccasin" alt="numpy@2.0.1">
  <img src="https://img.shields.io/badge/pandas-2.1.1-orange" alt="pandas@2.1.1">
  <img src="https://img.shields.io/badge/opencv-4.10.0.84-papayawhip" alt="opencv-python@4.10.0.84">
  <img src="https://img.shields.io/badge/streamlit-1.37.1-red" alt="streamlit@1.37.1">
</p> 


<img src="ss1.png"/>

---
**grayscale contrast**

<img src="ss3.png"/>

**enhance color contrast**
<img src="ss4.png"/>

## ⚙️Tech-Stack
- **Python**
- **OpenCV**
- **Streamlit**
- **Numpy**
- **Pandas**

## 🧤Image Preprocessing Steps

### Purpose
The `enhance_color_contrast` function is designed to preprocess an image by enhancing its color and contrast to make text more visible while reducing the effects of bleed-through. After enhancing the image, the function converts it into a black-and-white (binary) format, making it suitable for document analysis, OCR, or similar tasks where clear text visibility is crucial.

### Function Signature
```python
def enhance_color_contrast(uploaded_image):
```

### Parameters
- **`uploaded_image`**: 
  - **Type**: File-like object (e.g., an uploaded image file)
  - **Description**: This is the image file provided by the user. It is expected to be in a readable format like JPEG, PNG, etc.

### Returns
- **`bw_image`**:
  - **Type**: PIL Image object
  - **Description**: A black-and-white version of the processed image where the text is more visible, and the effects of bleed-through are minimized.

### Step-by-Step Processing

1. **Read the Image**
   ```python
   file_bytes = np.asarray(bytearray(uploaded_image.read()), dtype=np.uint8)
   image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
   ```
   - **Description**: Converts the uploaded file into an OpenCV-readable format. The image is decoded into a BGR color format.

2. **Check Image Validity**
   ```python
   if image is None:
       raise ValueError("Error: Unable to read the image. Please upload a valid image file.")
   ```
   - **Description**: Ensures that the image was loaded correctly. If the image is invalid, an error is raised.

3. **Convert Image to PIL Format**
   ```python
   pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
   ```
   - **Description**: Converts the image from OpenCV’s BGR format to RGB and then to a PIL Image object for easier manipulation.

4. **Enhance Contrast**
   ```python
   contrast_enhancer = ImageEnhance.Contrast(pil_image)
   pil_image = contrast_enhancer.enhance(1.5)
   ```
   - **Description**: Increases the contrast of the image by a factor of 1.5. This step makes the text stand out more against the background.

5. **Enhance Color Saturation**
   ```python
   color_enhancer = ImageEnhance.Color(pil_image)
   pil_image = color_enhancer.enhance(1.5)
   ```
   - **Description**: Enhances the color saturation by a factor of 1.5. This makes the colors in the image more vivid, which can further improve text visibility.

6. **Convert Back to OpenCV Format**
   ```python
   enhanced_image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
   ```
   - **Description**: Converts the enhanced image back to the BGR format for further processing in OpenCV.

7. **Apply Optional Denoising**
   ```python
   denoised_image = cv2.fastNlMeansDenoisingColored(enhanced_image, None, 10, 10, 7, 21)
   ```
   - **Description**: Applies mild denoising to reduce any remaining noise in the image, which may have been intensified by the previous enhancements.

8. **Convert Back to PIL Format**
   ```python
   final_pil_image = Image.fromarray(denoised_image)
   ```
   - **Description**: Converts the denoised image back to a PIL Image object for final processing.

9. **Convert to Grayscale**
   ```python
   grayscale_image = final_pil_image.convert('L')
   ```
   - **Description**: Converts the enhanced image to grayscale. This step prepares the image for binarization.

10. **Apply Binary Threshold for Black and White Conversion**
    ```python
    bw_image = grayscale_image.point(lambda x: 0 if x < 128 else 255, '1')
    ```
    - **Description**: Converts the grayscale image into a black-and-white (binary) image using a threshold value of 128. Pixels with a value below 128 are set to black, and pixels with a value of 128 or higher are set to white.

11. **Return the Final Image**
    ```python
    return bw_image
    ```
    - **Description**: The final black-and-white image is returned, with enhanced text visibility and reduced bleed-through.

### Example Usage
```python
# Assuming 'uploaded_file' is an image file object obtained from a file upload
processed_image = enhance_color_contrast(uploaded_file)
processed_image.show()  # Displays the processed black-and-white image
```

### Notes
- **Adjustable Parameters**: The contrast and color saturation factors can be adjusted to better suit the specific characteristics of the image. The default factors are set to 1.5, but they can be increased or decreased depending on the desired level of enhancement.
- **Denoising**: The denoising step is optional and can be adjusted or removed if the image is already clean or if noise reduction is not needed.

This function is particularly useful for preprocessing scanned documents, where text needs to be **clearly visible**, and **bleed-through** from the other side of the page needs to be minimized.