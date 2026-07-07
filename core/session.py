
from __future__ import annotations

import uuid
from datetime import datetime

import streamlit as st


def _create_chat(title: str) -> dict:
    return {
        "id": str(uuid.uuid4()),
        "title": title,
        "created_at": datetime.now().isoformat(),
        "messages": [],
        "title_status": "ready"   # NEW
    }


def initialize_session() -> None:

    if "chats" not in st.session_state:

        first_chat = _create_chat("Chat 1")

        st.session_state.chats = {
            first_chat["id"]: first_chat
        }

    if "active_chat" not in st.session_state:

        st.session_state.active_chat = next(
            iter(st.session_state.chats)
        )

    if "chat_counter" not in st.session_state:

        st.session_state.chat_counter = 2


def get_active_chat() -> dict:

    return st.session_state.chats[
        st.session_state.active_chat
    ]


def get_messages() -> list:

    return get_active_chat()["messages"]


def add_message(
    role: str,
    content: str
) -> None:

    get_active_chat()["messages"].append(
        {
            "role": role,
            "content": content
        }
    )


def new_chat() -> None:

    title = f"Chat {st.session_state.chat_counter}"

    chat = _create_chat(title)

    st.session_state.chats[chat["id"]] = chat

    st.session_state.active_chat = chat["id"]

    st.session_state.chat_counter += 1


def switch_chat(chat_id: str) -> None:

    st.session_state.active_chat = chat_id


def rename_chat(
    chat_id: str,
    title: str
) -> None:

    title = title.strip()

    if title:

        st.session_state.chats[chat_id]["title"] = title


def delete_chat(chat_id: str) -> None:

    if len(st.session_state.chats) == 1:
        return

    del st.session_state.chats[chat_id]

    st.session_state.active_chat = next(
        iter(st.session_state.chats)
    )


def clear_messages() -> None:

    get_messages().clear()


def total_messages() -> int:

    return sum(
        len(chat["messages"])
        for chat in st.session_state.chats.values()
    )
    
def should_generate_title() -> bool:
    """
    Returns True only when the active chat
    has received its first user message.
    """

    messages = get_messages()

    user_messages = [
        message
        for message in messages
        if message["role"] == "user"
    ]

    return len(user_messages) == 1

def set_title_generating() -> None:
    get_active_chat()["title"] = "Generating..."
    get_active_chat()["title_status"] = "generating"


def set_chat_title(title: str) -> None:
    title = title.strip()

    if title:
        get_active_chat()["title"] = title
        get_active_chat()["title_status"] = "ready"        
