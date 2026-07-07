
import streamlit as st


def load_css() -> None:

    st.markdown(
        """
        <style>

        /* Hide Streamlit branding */

        #MainMenu {
            visibility: hidden;
        }

        footer {
            visibility: hidden;
        }

        header {
            visibility: hidden;
        }

        /* Main page */

        .block-container{
            padding-top:2rem;
            padding-bottom:2rem;
            max-width:1400px;
        }

        /* Sidebar */

        section[data-testid="stSidebar"]{
            border-right:1px solid #2E3440;
        }

        section[data-testid="stSidebar"]{
            padding-top:1rem;
        }

        /* Buttons */

        .stButton button{

            width:100%;
            border-radius:12px;
            height:46px;
            font-weight:600;

            transition:all .2s ease;
        }

        .stButton button:hover{

            transform:translateY(-1px);

        }

        /* Chat Input */

        div[data-testid="stChatInput"]{

            margin-top:20px;

        }

        /* Chat Messages */

        div[data-testid="stChatMessage"]{

            border-radius:14px;

            padding:6px;

            margin-bottom:8px;

        }

        /* Code blocks */

        pre{

            border-radius:12px;

        }

        /* Scroll bar */

        ::-webkit-scrollbar{

            width:10px;

        }

        ::-webkit-scrollbar-thumb{

            border-radius:20px;

            background:#4B5563;

        }

        </style>
        """,
        unsafe_allow_html=True,
    )
