import streamlit as st
import os
# Reusable formatting / code


def render_image(path,width):
    """
    The use of this function is to render images
    """
    if not os.path.exists(path):
        st.warning(f"Image not found: {path}")
        return
    st.image(path,width=width)