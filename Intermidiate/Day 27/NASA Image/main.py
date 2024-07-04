import streamlit as st
import requests

api_key = "Caufy6Hl4LgVbSIYm77z5QeWE6ve57QNYf3fZLQm"

url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

response = requests.get(url)

content = response.json()
img_path = "img.png"
image = content['hdurl']

title = content['title']
res_image = requests.get(image)
with open(img_path, 'wb') as file:
    file.write(res_image.content)
description = content['explanation']

st.title(title)
st.image(img_path)
st.text(description)