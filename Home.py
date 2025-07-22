import streamlit as st

# Set Streamlit page config
st.set_page_config(
    page_title="AI Career Counselor",
    layout="centered",
)

# CSS Styles
st.markdown("""
<style>
body {
    background: linear-gradient(to right, #f0f8ff, #e6f0ff);
}
.main-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin-top: 5vh;
    text-align: center;
    background-color: white;
    padding: 2.5rem;
    border-radius: 16px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    max-width: 700px;
    margin-left: auto;
    margin-right: auto;
}
.title {
    font-size: 2.5rem;
    font-weight: bold;
    color: #2e8bc0;
    font-family: 'Segoe UI', sans-serif;
    margin-bottom: 0.5rem;
}
.subtitle {
    font-size: 1.2rem;
    color: #333333;
    margin-bottom: 2rem;
}
button.css-1q8dd3e {  /* Streamlit button primary style */
    background-color: #2e8bc0 !important;
    color: white !important;
    font-weight: bold !important;
    border-radius: 8px !important;
    padding: 0.6rem 1.2rem !important;
}
</style>
""", unsafe_allow_html=True)

# Home Page UI
with st.container():
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.markdown("<div class='title'>👩‍🎓 Welcome to AI Career Counselor</div>", unsafe_allow_html=True)
    st.markdown("""
        <div class='subtitle'>
        Find your ideal career path based on your interests, preferences, and strengths.<br><br>
        This tool uses intelligent mapping and personalized roadmaps to guide you through the career journey.
        </div>
    """, unsafe_allow_html=True)

    if st.button("🎯 Attempt Quiz to Know Your Best-Fit Career"):
        st.switch_page("pages/1_Career_Quiz.py")



    st.markdown("</div>", unsafe_allow_html=True)
