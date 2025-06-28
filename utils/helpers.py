import streamlit as st

# Reusable formatting / code


def render_image(path,width):
    """
    The use of this function is to render images
    """
    st.image(path,width=width)