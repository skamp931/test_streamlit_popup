import streamlit as st
import time

st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://www.example.com/image.jpg");
    }
   </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <link rel="stylesheet" type="text/css" href="https://www.example.com/style.css">
    """,
    unsafe_allow_html=True
)
