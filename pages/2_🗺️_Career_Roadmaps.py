import streamlit as st
from roadmaps import roadmap_css, get_roadmap_html

st.title("🗺️ Career Roadmaps")

if "top_3" in st.session_state:
    st.markdown(roadmap_css, unsafe_allow_html=True)
    for career, _ in st.session_state.top_3:
        with st.container():
            st.markdown(get_roadmap_html(career), unsafe_allow_html=True)
else:
    st.warning("Please complete the career quiz first to view personalized roadmaps.")
