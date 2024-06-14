import streamlit as st

option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"))

if st.checkbox('Show Camera : '):
    picture = st.camera_input("Take a picture")

    if picture:
        st.image(picture)