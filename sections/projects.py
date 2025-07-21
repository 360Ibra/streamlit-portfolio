# project_page.py
import streamlit as st
from utils.helpers import render_image

def show():
    st.title("📂 Project Portfolio")

    def display_project_card(title, subtitle, image_path, description, video_url=None, tags=[]):
        with st.container():
            col1, col2 = st.columns([1, 3])
            with col1:
                render_image(image_path, width=160)
            with col2:
                st.subheader(title)
                st.caption(subtitle)
                st.markdown(description)

                if video_url:
                    with st.expander("🎥 Watch Demo"):
                        st.video(video_url)

                if tags:
                    st.markdown("**Tech Stack:** " + ", ".join(tags))

            st.divider()

    # ✅ Example: Pose Estimation Project
    display_project_card(
        title="AI Injury Prevention App (Pose Estimation)",
        subtitle="Final Year Project • MTU • Jan – May 2024",
        image_path="assets/MTU.png",
        description="""
        Developed a real-time pose estimation Android app using MMPose. 
        Trained a deep learning model on the MPII dataset, converted it from PyTorch to ONNX and NCNN, 
        and deployed it with a cross-compiled MMDeploy library for Java integration.
        """,
        video_url="https://youtu.be/your_demo_link",  # Replace with your real link
        tags=["Python", "PyTorch", "ONNX", "NCNN", "Android", "CMake", "Computer Vision"]
    )

    # ✅ Add more cards for other projects similarly
