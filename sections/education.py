import streamlit as st
from utils.helpers import render_image

def show():
    st.title("Education")

    mtu_modules = [
        "Data Structures",
        "Web Development",
        "Object-Oriented Programming",
        "Database Management",
        "Mobile App Development",
        "Software Testing",
    ]

    ul_modules = [
        "INTRODUCTION TO SCIENTIFIC COMPUTING",
        "INTRODUCTION TO DEEP LEARNING AND FRAMEWORKS ",
        "Artificial Intelligence & Machine Learning ",
        "DATA ANALYTICS",
        "ADVANCED TOPICS SEMINARS AND PROJECT SPECIFICATION",
        "RISK, ETHICS, GOVERNANCE AND ARTIFICIAL INTELLIGENCE",
    ]

    def display_modules(title, caption, logo_path, modules):
        with st.container():
            col1, col2 = st.columns([1, 3])
            with col1:
                render_image(logo_path, width=120)

            with col2:
                st.subheader(title)
                st.caption(caption)
                for mod in modules:
                    with st.expander(f"📘 {mod}"):
                        st.markdown(f"Description and learning outcomes for **{mod}** can be added here.")

            st.divider()

    display_modules(
        title="Munster Technological University",
        caption="2021 – 2024 | BSc in Software Development",
        logo_path="assets/MTU.png",
        modules=mtu_modules
    )

    display_modules(
        title="University Of Limerick",
        caption="2024 – 2026 | MSc in Artificial Intelligence with Computer Vision",
        logo_path="assets/UL.png",
        modules=ul_modules
    )
