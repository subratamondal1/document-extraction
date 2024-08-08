import streamlit as st
from PIL import Image
from preprocess_image import grayscale_contrast

st.title("Document Extraction")

# Display logo in the sidebar
st.sidebar.image("logo.jpg", use_column_width=True)

# Image uploader in the sidebar
uploaded_image = st.sidebar.file_uploader("**Upload Image**",
                                          type=["jpg", "jpeg", "png"])

if uploaded_image:
  st.write("### Image Preview")

  # Display the original image
  # original_image = Image.open(uploaded_image)
  st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

  # Optionally, you can add a button to trigger processing
  if st.button("Process Image"):
    # Process the uploaded image
    preprocessed_image = grayscale_contrast(uploaded_image)

    if preprocessed_image:
      # Display the processed image
      st.write("### Processed Image")
      st.image(preprocessed_image,
               caption="Processed Image",
               use_column_width=True)
      st.success("Image processed successfully!")
    else:
      st.info("Please upload an image to see the results.")
