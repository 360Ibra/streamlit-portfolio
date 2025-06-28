# Main Streamlit file

from sections import about, projects, education, contact
import streamlit as st


pages = {
    "About Me" : about.show,
}

choice = st.sidebar.radio("Go to", list(pages.keys()))
pages[choice]()