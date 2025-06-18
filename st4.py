import streamlit as st

name = st.text_input("名前：")
st.write("結果", name)

text = st.text_area("長いテキスト")
st.write("結果", text)

with st.form(key = "nameinput"):
    family = st.text_input("姓：")
    name = st.text_input("名：")
    button = st.form_submit_button("送信")

if button:
    st.write("姓：", family, "、名：", name)

from PIL import Image

pic = st.camera_input("写真を撮る")

if pic:
    image = Image.open(pic)
    gray_image = image.convert("L")

    st.image(gray_image)