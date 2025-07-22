# pages/4_💬_Career_Chatbot.py

import streamlit as st
from chatbot_logic import get_chatbot_response

# Set Streamlit page config (MUST be first Streamlit call)
st.set_page_config(page_title="💬 Career Chatbot", layout="centered")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Page Title
st.title("💬 Career Chatbot")
st.caption("Ask me anything about careers, colleges, exams, alternatives, or even personal doubts.")

# Custom Chat UI Styling
st.markdown("""
<style>
.chat-message {
    display: flex;
    margin-bottom: 1rem;
}
.user-msg {
    justify-content: flex-end;
}
.bot-msg {
    justify-content: flex-start;
}
.bubble {
    max-width: 70%;
    padding: 0.8rem 1rem;
    border-radius: 16px;
    font-size: 1rem;
    line-height: 1.4;
}
.user-bubble {
    background-color: #daf1ff;
    color: #000;
    text-align: right;
    border-top-right-radius: 0;
}
.bot-bubble {
    background-color: #f0f0f0;
    color: #000;
    text-align: left;
    border-top-left-radius: 0;
}
.name-label {
    font-size: 0.75rem;
    font-weight: bold;
    margin-bottom: 0.2rem;
}
.user-name {
    text-align: right;
    margin-right: 0.5rem;
    color: #2e8bc0;
}
.bot-name {
    text-align: left;
    margin-left: 0.5rem;
    color: #666666;
}
</style>
""", unsafe_allow_html=True)

# Render previous messages
for msg in st.session_state.chat_history:
    # User message
    st.markdown(f"""
    <div class="chat-message user-msg">
        <div>
            <div class="name-label user-name">You</div>
            <div class="bubble user-bubble">{msg['user']}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Bot response
    st.markdown(f"""
    <div class="chat-message bot-msg">
        <div>
            <div class="name-label bot-name">Bot</div>
            <div class="bubble bot-bubble">{msg['bot']}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Chat input box
if user_input := st.chat_input("Type your question here..."):
    # Append user's message
    st.session_state.chat_history.append({"user": user_input, "bot": "..."})  # Temporary placeholder

    # Show user message immediately
    st.markdown(f"""
    <div class="chat-message user-msg">
        <div>
            <div class="name-label user-name">You</div>
            <div class="bubble user-bubble">{user_input}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Get bot's response
    with st.spinner("Thinking..."):
        bot_response = get_chatbot_response(user_input)

    # Replace the placeholder with actual response
    st.session_state.chat_history[-1]["bot"] = bot_response

    # Show bot response
    st.markdown(f"""
    <div class="chat-message bot-msg">
        <div>
            <div class="name-label bot-name">Bot</div>
            <div class="bubble bot-bubble">{bot_response}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
