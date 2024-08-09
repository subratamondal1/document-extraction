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

<img src="ss3.png"/>

## ⚙️Tech-Stack
- **Python**
- **OpenCV**
- **Streamlit**
- **Numpy**
- **Pandas**

## 🧤Image Preprocessing Steps
1. **Image Reading**:
Reads the uploaded image file and decodes it into a format that OpenCV can process. This converts the image from a file-like object to a NumPy array.

   ```python
     file_bytes = np.asarray(bytearray(uploaded_image.read()), dtype=np.uint8)
     image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
     ```

3. **Grayscale Conversion**:
Converts the color image to a grayscale image. This simplifies the image data, making it easier to process for text extraction.

   ```python
     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
     ```

4. **Bilateral Filtering**:
Applies a bilateral filter to reduce noise while preserving edges. This helps maintain the integrity of text features, making them clearer for subsequent processing.

   ```python
     filtered = cv2.bilateralFilter(gray, d=9, sigmaColor=75, sigmaSpace=75)
     ```

5. **Adaptive Thresholding**:
Converts the filtered grayscale image into a binary image using adaptive thresholding. This technique enhances the contrast between the text and the background, making the text more distinguishable.

   ```python
     adaptive_thresh = cv2.adaptiveThreshold(filtered, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
     ```

6. **Morphological Operations**:
Applies morphological closing to the binary image. This operation fills small holes in the text and connects nearby text components, enhancing the overall appearance of the text for better extraction.

   ```python
     kernel = np.ones((3, 3), np.uint8)
     morph = cv2.morphologyEx(adaptive_thresh, cv2.MORPH_CLOSE, kernel)
     ```

7. **Conversion to PIL Image**:
Converts the processed NumPy array (binary image) back into a PIL Image object. This format is often required for further processing or display in applications like Streamlit.

   ```python
     pil_image = Image.fromarray(morph)
     ```

These preprocessing steps collectively enhance the visibility of text in images while reducing noise and interference from other elements, making it easier for text extraction models to accurately read the text.