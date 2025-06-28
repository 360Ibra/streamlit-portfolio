# Intro and interests
import streamlit as st
from utils.helpers import render_image

def show():
    st.title("Ibrahim Aminu")
    st.write("Hey, my name is Ibrahim. I'm a software engineer and process engineer passionate about computer vision and AI. Currently, I work at Boston Scientific, building proof-of-concept automation and vision systems, while pursuing my master's in Computer Vision and AI. I focus on using AI as a tool to build practical, impactful solutions, especially in robotics and medical imaging. Outside work, I enjoy learning new technologies, reading research papers, and contributing to community projects.")
    render_image("assets/profile_header.png",300)