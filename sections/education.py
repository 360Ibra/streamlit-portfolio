# Modules and SKills

import streamlit as st

from utils.helpers import render_image


def show():
    st.title("Education")
    ul_modules = ["Data Structures", "Computer Vision", "Control Systems"]
    mtu_modules = ["Data Structures", "Computer Vision", "Control Systems"]

    with st.container():
        col1, col2 = st.columns([1, 3])
        with  col1:
            render_image("assets/MTU.png", width=300)

        with col2:
            st.subheader("Munster Technological University")
            st.caption("2021 – 2024 | BSc in Software Development")
            st.markdown("Key modules: ...")

            for mod in mtu_modules:
                if st.button(mod):
                    st.write(f"Details about {mod}")
        st.divider()

        col1, col2 = st.columns([1, 3])
        with  col1:
            render_image("assets/UL.png", width=300)

        with col2:
            st.subheader("University Of Limerick")
            st.caption("2024 – 2026 | MSc in Artificial Intelligence with Computer Vision")
            st.markdown("Key modules: ...")

            # for mod in ul_modules:
            #     if st.button(mod):
            #         st.write(f"Details about {mod}")
