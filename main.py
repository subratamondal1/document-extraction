import streamlit as st
from PIL import Image

# Title of the app
st.title("Document Extraction")

# Image uploader in the sidebar
uploaded_image = st.sidebar.file_uploader("**Upload Image**",
                                          type=["jpg", "jpeg", "png"])

# Main content area
st.write("### Image Preview")

if uploaded_image is not None:
  # Open the uploaded image using PIL
  image = Image.open(uploaded_image)

  # Display the original image
  st.image(image, caption="Uploaded Image", use_column_width=True)

  # Placeholder for processed image (for demonstration, we'll just display the same image)
  processed_image = image  # Replace this with your image processing function

  # Display the processed image
  st.write("### Processed Image")
  st.image(processed_image, caption="Processed Image", use_column_width=True)

  # Optionally, you can add a button to trigger processing
  if st.sidebar.button("Process Image"):
    # Add your image processing logic here
    st.success("Image processed successfully!")
else:
  st.info("Please upload an image to see the results.")
