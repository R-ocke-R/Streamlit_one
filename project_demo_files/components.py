import streamlit as st
import os





# Create a folder to store uploaded images if it doesn't exist
UPLOAD_FOLDER = "Image_data_grow"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Display file uploader
#uploaded_photo = st.file_uploader("Upload a photo")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])


# Check if file is uploaded
if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    
    # Display a submit button
if st.button("Save Image"):
    # Save the uploaded image to the specified folder
    with open(os.path.join(UPLOAD_FOLDER, uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getvalue())
    
    # Display a success message
    st.success(f"Image '{uploaded_file.name}' saved successfully in '{UPLOAD_FOLDER}' folder.")
