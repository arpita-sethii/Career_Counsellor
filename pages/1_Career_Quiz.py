import streamlit as st
import matplotlib.pyplot as plt
from collections import defaultdict
from recommender import get_top_careers

st.write("### Please answer the following questions to find your best-fit career:")

# Quiz Questions
questions = [
    {
        "q": "Which activity sounds more fun to you?",
        "options": {
            "a": {"text": "Creating digital art", "careers": ["UI/UX Designer", "Content Creator"]},
            "b": {"text": "Analyzing statistics", "careers": ["Data Scientist", "AI/ML Engineer"]},
            "c": {"text": "Diagnosing medical symptoms", "careers": ["Doctor", "Psychologist"]}
        }
    },
    {
        "q": "How do you usually solve problems?",
        "options": {
            "a": {"text": "Using data and logic", "careers": ["Engineer", "Data Scientist", "Bioinformatician"]},
            "b": {"text": "Using creativity and emotions", "careers": ["Psychologist", "Content Creator", "Digital Marketer"]},
            "c": {"text": "Hands-on experimentation", "careers": ["Mechatronics Engineer", "Health Tech Innovator"]}
        }
    },
    {
        "q": "Which career day stall would attract you the most?",
        "options": {
            "a": {"text": "NASA exhibit with rockets", "careers": ["Space Scientist", "Engineer"]},
            "b": {"text": "Hospital surgery simulation", "careers": ["Doctor", "Health Tech Innovator"]},
            "c": {"text": "App design and gaming booth", "careers": ["Game Developer", "UI/UX Designer"]}
        }
    },
    {
        "q": "What type of news do you follow more?",
        "options": {
            "a": {"text": "Tech innovations", "careers": ["AI/ML Engineer", "Mechatronics Engineer"]},
            "b": {"text": "Business startups", "careers": ["Entrepreneur", "Product Manager"]},
            "c": {"text": "Mental health awareness", "careers": ["Psychologist", "Doctor"]}
        }
    },
    {
        "q": "What would you love to build?",
        "options": {
            "a": {"text": "A robot or automation tool", "careers": ["Mechatronics Engineer", "Engineer"]},
            "b": {"text": "An audience on social media", "careers": ["Content Creator", "Digital Marketer"]},
            "c": {"text": "A cure for a disease", "careers": ["Doctor", "Bioinformatician"]}
        }
    },
    {
        "q": "What is your ideal work style?",
        "options": {
            "a": {"text": "Solo deep work & coding", "careers": ["Game Developer", "Data Scientist"]},
            "b": {"text": "Team-based strategy & pitching", "careers": ["Product Manager", "Entrepreneur"]},
            "c": {"text": "Client-based consultation", "careers": ["Psychologist", "Legal Consultant"]}
        }
    },
    {
        "q": "Which elective would you prefer in school?",
        "options": {
            "a": {"text": "Coding or robotics", "careers": ["Engineer", "Game Developer", "Mechatronics Engineer"]},
            "b": {"text": "Art or media studies", "careers": ["UI/UX Designer", "Content Creator"]},
            "c": {"text": "Biology lab or healthcare club", "careers": ["Doctor", "Health Tech Innovator"]}
        }
    },
    {
        "q": "What do you believe creates more impact?",
        "options": {
            "a": {"text": "Designing tech that helps people", "careers": ["Engineer", "Health Tech Innovator"]},
            "b": {"text": "Telling powerful stories", "careers": ["Content Creator", "Digital Marketer"]},
            "c": {"text": "Solving policy or legal issues", "careers": ["Legal Consultant", "Entrepreneur"]}
        }
    },
    {
        "q": "What do people say you're good at?",
        "options": {
            "a": {"text": "Solving logic puzzles or coding", "careers": ["Data Scientist", "Game Developer"]},
            "b": {"text": "Listening and giving advice", "careers": ["Psychologist", "Doctor"]},
            "c": {"text": "Creativity and visual design", "careers": ["UI/UX Designer", "Content Creator"]}
        }
    },
    {
        "q": "If money and effort were no object, what would you learn first?",
        "options": {
            "a": {"text": "Machine learning and AI", "careers": ["AI/ML Engineer", "Data Scientist"]},
            "b": {"text": "Video editing and content creation", "careers": ["Content Creator", "Digital Marketer"]},
            "c": {"text": "Startup and business building", "careers": ["Entrepreneur", "Product Manager"]}
        }
    }
]

career_descriptions = {
    "Data Scientist": "Works with data, statistics, and machine learning to uncover insights.",
    "Doctor": "Practices medicine to diagnose and treat health conditions.",
    "Engineer": "Solves real-world problems through technical and mechanical design.",
    "UI/UX Designer": "Designs intuitive and aesthetic user interfaces and experiences.",
    "AI/ML Engineer": "Builds intelligent systems using artificial intelligence models.",
    "Game Developer": "Creates interactive games using logic, design, and storytelling.",
    "Psychologist": "Studies human behavior and provides mental health support.",
    "Product Manager": "Oversees product development, balancing user needs and business goals.",
    "Entrepreneur": "Creates and manages new businesses or startups, taking on financial risks.",
    "Content Creator": "Produces engaging content for social media, blogs, and video platforms.",
    "Digital Marketer": "Promotes brands and products using online tools like SEO, social media, and ads.",
    "Bioinformatician": "Applies computational methods to analyze biological and genetic data.",
    "Health Tech Innovator": "Combines healthcare knowledge with technology to improve medical outcomes.",
    "Mechatronics Engineer": "Integrates mechanical, electrical, and computer systems in automated devices.",
    "Legal Consultant": "Provides legal advice in areas like contracts, technology law, and compliance.",
    "Environmental Scientist": "Studies the environment and develops solutions for sustainability and pollution control.",
    "Space Scientist": "Conducts research related to space, satellites, astrophysics, and space missions."
}

# Quiz UI

user_answers = []
with st.form("quiz_form"):
    for i, q in enumerate(questions):
        options = [f"{k}) {v['text']}" for k, v in q["options"].items()]
        choice = st.radio(f"**Q{i+1}. {q['q']}**", options, key=f"q{i}")
        user_answers.append(choice[0])
    submitted = st.form_submit_button("Get My Career Recommendations")

# ⬇️ Now paste your block here
if submitted:
    # 1. Calculate career scores
    career_scores = defaultdict(int)
    for i, choice in enumerate(user_answers):
        careers = questions[i]["options"][choice]["careers"]
        for career in careers:
            career_scores[career] += 1

    # 2. Get top 3 careers using helper function
    top_3 = get_top_careers(career_scores)
    st.session_state.top_3 = top_3


    # 3. Show Top Career Matches
    st.subheader("🔮 Your Top Career Matches:")
    for career, score in top_3:
        st.markdown(f"**🎯 {career} (Score: {score})**")
        st.write(career_descriptions.get(career, "Description not available."))

    # 4. Visualize Score Breakdown
    st.subheader("📊 Score Breakdown")
    sorted_scores = sorted(career_scores.items(), key=lambda x: x[1], reverse=True)
    labels, values = zip(*sorted_scores[:6])
    fig, ax = plt.subplots()
    ax.barh(labels, values, color='skyblue')
    ax.set_xlabel("Score")
    ax.set_title("Top Career Matches")
    ax.invert_yaxis()
    st.pyplot(fig)