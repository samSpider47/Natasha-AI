
import streamlit as st

from core.session import get_messages


def render_chat_window() -> None:
    """
    Render the complete chat conversation.
    """

    messages = get_messages()

    if not messages:

        st.info(
            """
👋 Welcome to **Natasha AI**

I can soon help you with:

- 💬 Natural conversations
- 🧠 Long-term memory
- 🔍 RAG over documents
- 🛠️ Tool calling
- 🤖 Agentic AI workflows
- 📄 Code generation

Start by typing a message below.
"""
        )

        return

    for message in messages:

        role = message["role"]
        content = message["content"]

        avatar = "🤖"

        if role == "user":
            avatar = "👤"

        with st.chat_message(
            role,
            avatar=avatar
        ):
            st.markdown(content)
