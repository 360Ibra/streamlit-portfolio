# Intro and interests
import streamlit as st
from utils.helpers import render_image

def show():
    st.title("Ibrahim Aminu")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write(
            "Hey! I’m Ibrahim, a determined software engineer passionate about building practical, impactful solutions. "
            "My favorite language is Python, and I love exploring AI, machine learning, computer vision, and software development. "
            "I currently work at Boston Scientific and am also pursuing my master’s in Computer Vision and AI.\n\n"
            "Check out my projects, education, and contact info to learn more!"
        )

    with col2:
        render_image("assets/profile_header.png", 300)

