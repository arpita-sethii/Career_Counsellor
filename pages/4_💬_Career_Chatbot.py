# pages/4_💬_Career_Chatbot.py

import streamlit as st
from chatbot_logic import get_chatbot_response

# Page config
st.set_page_config(page_title="💬 Career Chatbot", layout="centered")

# --- Chat History Setup ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --- Styling for Chat Bubbles ---
st.markdown("""
<style>
.user-bubble, .bot-bubble {
    padding: 0.8rem 1rem;
    border-radius: 15px;
    margin: 0.5rem 0;
    max-width: 80%;
    line-height: 1.5;
}
.user-bubble {
    background-color: #daf1ff;
    align-self: flex-end;
    margin-left: auto;
    text-align: right;
}
.bot-bubble {
    background-color: #f0f0f0;
    align-self: flex-start;
    margin-right: auto;
}
.chat-container {
    display: flex;
    flex-direction: column;
}
</style>
""", unsafe_allow_html=True)

# --- Header ---
import streamlit as st
from chatbot_logic import get_chatbot_response

st.set_page_config(page_title="💬 Career Chatbot", layout="centered")

st.title("💬 Career Chatbot")
st.caption("Ask me anything about careers, colleges, exams, alternatives, etc.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Show previous messages
for chat in st.session_state.chat_history:
    with st.chat_message("user"):
        st.markdown(chat["user"])
    with st.chat_message("assistant"):
        st.markdown(chat["bot"])

# Accept user input
if user_input := st.chat_input("Type your question:"):
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.spinner("Thinking..."):
        bot_response = get_chatbot_response(user_input)

    with st.chat_message("assistant"):
        st.markdown(bot_response)

    # Save chat history and avoid infinite loop
    st.session_state.chat_history.append({"user": user_input, "bot": bot_response})
