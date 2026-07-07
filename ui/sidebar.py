
import streamlit as st

from core.session import (
    new_chat,
    switch_chat,
)

from documents.rag_service import rag_service


def render_sidebar() -> None:

    if "indexed_files" not in st.session_state:
        st.session_state.indexed_files = set()

    with st.sidebar:

        st.title("🤖 Natasha AI")

        st.divider()

        # -----------------------------
        # Chats
        # -----------------------------
        if st.button(
            "➕ New Chat",
            use_container_width=True
        ):
            new_chat()
            st.rerun()

        st.subheader("Chats")

        for chat_id, chat in st.session_state.chats.items():

            title = chat.get("title", "Untitled Chat")

            if st.button(
                title,
                key=chat_id,
                use_container_width=True
            ):
                switch_chat(chat_id)
                st.rerun()

        st.divider()

        # -----------------------------
        # Documents
        # -----------------------------
        st.subheader("📄 Documents")

        uploaded_files = st.file_uploader(
            "Upload PDF",
            type=["pdf"],
            accept_multiple_files=True,
            key="uploaded_documents"
        )

        if uploaded_files:

            for uploaded_file in uploaded_files:

                if uploaded_file.name in st.session_state.indexed_files:
                    continue

                with st.spinner(
                    f"Indexing {uploaded_file.name}..."
                ):

                    indexed = rag_service.index_document(
                        uploaded_file
                    )

                st.session_state.indexed_files.add(
                    uploaded_file.name
                )

                if indexed:

                    st.success(
                        f"✅ {uploaded_file.name} indexed successfully."
                    )

                else:

                    st.info(
                        f"ℹ️ {uploaded_file.name} is already indexed."
                    )

        if st.session_state.indexed_files:

            st.divider()

            st.subheader("Indexed Documents")

            for file_name in sorted(
                st.session_state.indexed_files
            ):

                st.write(f"📄 {file_name}")
