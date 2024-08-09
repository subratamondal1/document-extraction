import streamlit as st
from PIL import Image
from preprocess_image import grayscale_contrast
import io

st.markdown("<center><h1>📜📄 Document Extraction</h1></center>",
            unsafe_allow_html=True)

# Display logo in the sidebar
st.sidebar.image("logo.jpg", use_column_width=True)

# Image uploader in the sidebar
uploaded_image = st.sidebar.file_uploader("**Upload Image**",
                                          type=["jpg", "jpeg", "png"])

if uploaded_image:
    # Process the uploaded image
    preprocessed_image = grayscale_contrast(uploaded_image)

    # Create two columns for side-by-side display
    col1, col2 = st.columns(2)

    with col1:
        st.write("#### `Original Image`")
        st.image(uploaded_image,
                 caption="Uploaded Image",
                 use_column_width=True)

    with col2:
        st.write("#### `Processed Image`")
        st.image(preprocessed_image,
                 caption="Processed Image",
                 use_column_width=True)

    # Convert the preprocessed image to bytes for downloading
    img_byte_arr = io.BytesIO()
    preprocessed_image.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)

    # Add a download button
    st.download_button(
        label="Download Processed Image",
        data=img_byte_arr,
        file_name="processed_image.png",
        mime="image/png"
    )

    # Display success message
    st.success("Image processed successfully!")
else:
    st.info("Please upload an image to see the results.")

# Feedback and suggestions section in the sidebar
st.sidebar.info("[Feedback & Suggestions](mailto:subrata@thealgohype.com)")