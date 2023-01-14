import streamlit as st
from PIL import Image

camera_image = st.camera_input("Camera")

if camera_image:
    # Create a Pillow Image instance
    img = Image.open(camera_image)

    # Convert the pillow image to grayscale
    gray_img = img.convert("L")

    # fRander the grayscale image on the webpage
    st.image(gray_img)


