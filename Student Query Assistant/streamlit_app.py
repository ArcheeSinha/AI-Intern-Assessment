import streamlit as st
import pandas as pd
import os

from utils.chatbot import get_response
from utils.validator import validate_query
from utils.logger import save_conversation

# =====================================
# Page Config
# =====================================

st.set_page_config(
    page_title="Student Query Assistant",
    page_icon="🤖",
    layout="wide"
)

# =====================================
# Sidebar
# =====================================

with st.sidebar:

    st.title("🎓 Student Assistant")

    st.markdown("""
    ### Topics Supported

    - Programming
    - AI / Machine Learning
    - Career Guidance
    - Interview Preparation
    """)

    if st.button("🗑️ Clear Chat"):

        st.session_state.chat_history = []

        st.rerun()

# =====================================
# Main Page
# =====================================

st.title("🤖 AI-Powered Student Query Assistant")

st.caption(
    "Powered by Gemini 2.5 Flash"
)

# =====================================
# Session State
# =====================================

if "chat_history" not in st.session_state:

    st.session_state.chat_history = []

# =====================================
# Chat Input
# =====================================

user_query = st.chat_input(
    "Ask your question..."
)

# =====================================
# Process Query
# =====================================

if user_query:

    if not validate_query(user_query):

        st.error(
            "Please enter a valid question."
        )

    else:

        with st.spinner(
            "Generating response..."
        ):

            answer = get_response(
                user_query
            )

        save_conversation(
            user_query,
            answer
        )

        st.session_state.chat_history.append(
            {
                "user": user_query,
                "assistant": answer
            }
        )

# =====================================
# Display Chat
# =====================================

for chat in st.session_state.chat_history:

    with st.chat_message("user"):

        st.write(chat["user"])

    with st.chat_message("assistant"):

        st.write(chat["assistant"])

# =====================================
# Download Logs
# =====================================

log_file = "logs/conversations.csv"

if os.path.exists(log_file):

    st.divider()

    st.subheader(
        "📥 Download Conversation Logs"
    )

    df = pd.read_csv(log_file)

    csv_data = df.to_csv(
        index=False
    )

    st.download_button(
        label="Download CSV",
        data=csv_data,
        file_name="conversation_logs.csv",
        mime="text/csv"
    )