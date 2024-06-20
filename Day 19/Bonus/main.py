import streamlit as st
from PIL import Image

with st.expander("Start Camera"):
# Start the camera
    camera_image = st.camera_input("Camera")


if camera_image:
#Create a pillow image instance 
    img = Image.open(camera_image)

    #Convert the pillow image to grayscale
    gray_img = img.convert("L")

    #Render the image and convert the image into grayscale
    st.image(gray_img)
    print("Permission Accepted")

else:
    print("Please grant access to your camera")