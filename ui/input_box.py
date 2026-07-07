
import streamlit as st

from core.session import add_message


def render_input_box():

    st.divider()

    with st.form("chat_form", clear_on_submit=True):

        user_prompt = st.text_area(
            "Message",
            placeholder="Type your message here...",
            label_visibility="collapsed",
            height=90
        )

        submitted = st.form_submit_button(
            "🚀 Send",
            use_container_width=True
        )

    if submitted:

        if user_prompt.strip() == "":
            st.warning("Please enter a message.")
            return

        add_message(
            "user",
            user_prompt
        )

        # Temporary assistant response.
        # This will be replaced with LangGraph later.

        assistant_reply = f"""You said {user_prompt}"""

        add_message(
            "assistant",
            assistant_reply
        )

        st.rerun()
