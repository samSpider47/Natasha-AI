import streamlit as st

from core.session import (
    add_message,
    get_messages,
    initialize_session,
    set_title_generating,
    set_chat_title,
    should_generate_title
)

from services.chat_service import chat_service
from services.title_service import title_service
from services.memory_service import memory_service

from ui.chat_window import render_chat_window
from ui.sidebar import render_sidebar
from ui.styles import load_css


st.set_page_config(
    page_title="Natasha AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)


def main() -> None:

    initialize_session()

    load_css()

    render_sidebar()

    st.title("🤖 Natasha AI")

    st.caption("Powered by LangGraph + Groq")

    st.divider()

    render_chat_window()

    prompt = st.chat_input("Message Natasha...")

    if prompt:

        # -------------------------
        # 1. Save user message (session)
        # -------------------------
        add_message("user", prompt)

        # -------------------------
        # 2. Save user message (ChromaDB memory)
        # -------------------------
        memory_service.add_memory(
            user_id="default_user",
            text=prompt,
            metadata={"role": "user"}
        )

        # -------------------------
        # 3. Generate title (first message only)
        # -------------------------
        if should_generate_title():

            set_title_generating()

            title = title_service.generate_title(prompt)

            set_chat_title(title)

        # -------------------------
        # 4. Retrieve memory context
        # -------------------------
        memories = memory_service.search_memory(prompt)

        memory_context = "\n".join(memories) if memories else ""

        # -------------------------
        # 5. Build chat history + memory injection
        # -------------------------
        history = get_messages()

        if memory_context:

            history = [
                {
                    "role": "user",
                    "content": f"[MEMORY CONTEXT]\n{memory_context}"
                }
            ] + history

        # -------------------------
        # 6. Stream assistant response
        # -------------------------
        with st.chat_message("assistant"):

            response = st.write_stream(
                chat_service.stream_message(history)
            )

        # -------------------------
        # 7. Save assistant response
        # -------------------------
        add_message("assistant", response)

        st.rerun()


if __name__ == "__main__":
    main()