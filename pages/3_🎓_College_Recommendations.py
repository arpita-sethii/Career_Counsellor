import streamlit as st
from recommender import get_colleges_for_career
from roadmaps import career_roadmaps  # optional, if you want career list

st.title("🎓 College Recommendations")

if "top_3" in st.session_state:
    for career, _ in st.session_state.top_3:
        st.markdown(f"#### 📘 Colleges for **{career}**")
        matched = get_colleges_for_career(career)
        if matched.empty:
            st.info(f"No colleges found for {career}.")
        else:
            for _, row in matched.iterrows():
                st.markdown(f"""
                <div style='background-color:#f0f8ff; padding:10px; border-radius:10px; margin-bottom:10px;'>
                    <b>🏫 {row['college']}</b><br>
                    📍 {row['location']}<br>
                    📝 Entrance: {row['exam']}<br>
                    🔗 <a href="{row['website']}" target="_blank">Visit Website</a>
                </div>
                """, unsafe_allow_html=True)
else:
    st.warning("Please complete the career quiz first to get personalized college recommendations.")
