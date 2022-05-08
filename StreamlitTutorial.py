import streamlit as st
from PIL import Image

st.title("ALGO May 8th tutorial")
st.write("hello world")

image = Image.open('cat.jpg')

st.image(image, caption='A cat')