
from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="GenAI Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------- SESSION STATE ----------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "theme" not in st.session_state:
    st.session_state.theme = "Dark"

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown("# 🤖 GenAI")
    st.caption("Your AI-powered assistant")

    st.divider()

    st.markdown("### Appearance")

  

with st.sidebar:
    st.markdown("### Appearance")

    theme = st.segmented_control(
        "Choose theme",
        options=["☀️ Light", "🌙 Dark"],
        default="🌙 Dark" if st.session_state.theme == "Dark" else "☀️ Light",
        label_visibility="collapsed",
    )

    if theme is not None:
        st.session_state.theme = (
            "Dark" if theme == "🌙 Dark" else "Light"
        )

    dark = st.session_state.theme == "Dark"

    st.divider()

    st.markdown("### Conversation")

    st.metric("Messages", len(st.session_state.chat_history))

    if st.button("🗑️ Clear conversation", use_container_width=True):
        st.session_state.chat_history = []
        st.rerun()

    st.divider()

    st.markdown("### About")
    st.caption(
        "Powered by LangChain and Groq. "
        "Ask questions, explore ideas, and learn something new."
    )

    st.markdown("---")
    st.caption("Made with ❤️ using Streamlit")

# ---------------- THEME COLORS ----------------

if dark:
    bg = "#0E1117"
    panel = "#161B22"
    text = "#F0F3F6"
    muted = "#B0BAC7"
    border = "#30363D"
    accent = "#A99BFF"
    user_bubble = "#302852"
    assistant_bubble = "#191F29"
    input_bg = "#161B22"
else:
    bg = "#FFFFFF"
    panel = "#FFFFFF"
    text = "#1F2937"
    muted = "#596579"
    border = "#D8DEE8"
    accent = "#5548C8"
    user_bubble = "#EEEAFE"
    assistant_bubble = "#FFFFFF"
    input_bg = "#FFFFFF"
    assistant_bubble = "#FFFFFF"

# ---------------- CUSTOM CSS ----------------


# ---------------- CUSTOM CSS ----------------

st.markdown(
    f"""
    <style>
    /* Main application backgrounds */
    .stApp,
    [data-testid="stAppViewContainer"],
    [data-testid="stMain"],
    [data-testid="stHeader"] {{
        background-color: {bg} !important;
        color: {text} !important;
    }}

    .block-container {{
        max-width: 1000px;
        padding-top: 2rem;
        padding-bottom: 7rem;
    }}

    /* Sidebar */
    [data-testid="stSidebar"],
    [data-testid="stSidebar"] > div:first-child {{
        background-color: {panel} !important;
        border-right: 1px solid {border};
    }}

    /* General text */
    .stApp h1,
    .stApp h2,
    .stApp h3,
    .stApp p,
    .stApp label,
    .stApp li,
    .stApp [data-testid="stMarkdownContainer"],
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] label {{
        color: {text};
    }}

    [data-testid="stCaptionContainer"],
    [data-testid="stCaptionContainer"] p {{
        color: {muted} !important;
    }}

    /* Header card */
    .hero {{
        background-color: {panel};
        border: 1px solid {border};
        border-radius: 22px;
        padding: 28px;
        margin-bottom: 25px;
    }}

    .hero-title {{
        font-size: 32px;
        font-weight: 750;
        letter-spacing: -1px;
        color: {text} !important;
        margin-bottom: 8px;
    }}

    .hero-subtitle {{
        color: {muted} !important;
        font-size: 15px;
        line-height: 1.7;
    }}

    .status {{
        display: inline-block;
        padding: 6px 12px;
        border-radius: 20px;
        background-color: {user_bubble};
        color: {accent} !important;
        font-size: 12px;
        font-weight: 600;
        margin-bottom: 16px;
    }}

    /* Chat message containers */
    [data-testid="stChatMessage"] {{
        background-color: {assistant_bubble} !important;
        border: 1px solid {border};
        border-radius: 16px;
        padding: 14px 18px;
        margin-bottom: 14px;
    }}

    [data-testid="stChatMessage"] p,
    [data-testid="stChatMessage"] li,
    [data-testid="stChatMessage"] h1,
    [data-testid="stChatMessage"] h2,
    [data-testid="stChatMessage"] h3,
    [data-testid="stChatMessage"] strong {{
        color: {text} !important;
        line-height: 1.75;
    }}

    /* Chat input */
    [data-testid="stChatInput"] {{
        background-color: {input_bg} !important;
        border: 1px solid {border} !important;
        border-radius: 16px !important;
    }}

    [data-testid="stChatInput"] > div {{
        background-color: {input_bg} !important;
        border-radius: 16px !important;
    }}

    [data-testid="stChatInput"] textarea {{
        background-color: {input_bg} !important;
        color: {text} !important;
        -webkit-text-fill-color: {text} !important;
        border-color: {border} !important;
    }}

    [data-testid="stChatInput"] textarea::placeholder {{
        color: {muted} !important;
        -webkit-text-fill-color: {muted} !important;
    }}

    /* Chat input send button */
    [data-testid="stChatInput"] button {{
        background-color: transparent !important;
        color: {accent} !important;
        border: none !important;
    }}

    [data-testid="stChatInput"] button svg {{
        fill: {accent} !important;
        color: {accent} !important;
    }}

    /* Bottom area behind the chat input */
    [data-testid="stBottom"] {{
        background-color: {bg} !important;
    }}

    [data-testid="stBottom"] > div,
    [data-testid="stBottom"] [data-testid="stBottomBlockContainer"] {{
        background-color: {bg} !important;
    }}

    [data-testid="stBottom"]::before {{
        background: {bg} !important;
    }}

    /* Buttons */
    .stButton > button {{
        background-color: {panel} !important;
        color: {text} !important;
        border: 1px solid {border} !important;
        border-radius: 12px;
        min-height: 42px;
        transition: all 0.2s ease;
    }}

    .stButton > button:hover {{
        border-color: {accent} !important;
        color: {accent} !important;
    }}

    /* Light and dark toggle */
    [data-testid="stSegmentedControl"] {{
        background-color: {panel} !important;
        border: 1px solid {border};
        border-radius: 12px;
    }}

    [data-testid="stSegmentedControl"] label {{
        color: {text} !important;
    }}

    /* Metrics */
    [data-testid="stMetric"] {{
        background-color: {panel} !important;
        padding: 14px;
        border: 1px solid {border};
        border-radius: 14px;
    }}

    [data-testid="stMetricLabel"],
    [data-testid="stMetricValue"] {{
        color: {text} !important;
    }}

    /* Links, dividers and code */
    .stApp a {{
        color: {accent} !important;
    }}

    hr {{
        border-color: {border} !important;
    }}

    code {{
        color: {accent} !important;
    }}

    /* Scrollbars */
    * {{
        scrollbar-color: {border} {bg};
    }}
    </style>
    """,
    unsafe_allow_html=True,
)


# ---------------- HEADER ----------------

st.markdown(
    """
    <div class="hero">
        <div class="status">● AI ASSISTANT</div>
        <div class="hero-title">Your AI companion 🤖</div>
        <div class="hero-subtitle">
            Ask questions, solve problems, brainstorm ideas,
            or explore something completely new.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# ---------------- LLM ----------------
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.0,
)

# ---------------- CHAT HISTORY ----------------
for message in st.session_state.chat_history:
    avatar = "👤" if message["role"] == "user" else "🤖"

    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# ---------------- WELCOME SCREEN ----------------
if not st.session_state.chat_history:
    st.markdown("### 👋 Welcome! What would you like to explore?")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            f"""
            <div style="background:{panel};border:1px solid {border};
            border-radius:14px;padding:18px;margin-bottom:12px;">
                <div style="font-size:24px;">💡</div>
                <b style="color:{text};">Learn something</b>
                <p style="color:{muted};font-size:13px;">
                    Understand concepts and discover new ideas.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
            <div style="background:{panel};border:1px solid {border};
            border-radius:14px;padding:18px;">
                <div style="font-size:24px;">🧑‍💻</div>
                <b style="color:{text};">Coding assistant</b>
                <p style="color:{muted};font-size:13px;">
                    Debug code and understand programming.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            f"""
            <div style="background:{panel};border:1px solid {border};
            border-radius:14px;padding:18px;margin-bottom:12px;">
                <div style="font-size:24px;">✍️</div>
                <b style="color:{text};">Writing & creativity</b>
                <p style="color:{muted};font-size:13px;">
                    Draft content and brainstorm possibilities.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
            <div style="background:{panel};border:1px solid {border};
            border-radius:14px;padding:18px;">
                <div style="font-size:24px;">📚</div>
                <b style="color:{text};">Study & research</b>
                <p style="color:{muted};font-size:13px;">
                    Summarize topics and explore technical subjects.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ---------------- USER INPUT ----------------
user_prompt = st.chat_input("Message your AI assistant...")

if user_prompt:
    with st.chat_message("user", avatar="👤"):
        st.markdown(user_prompt)

    st.session_state.chat_history.append(
        {"role": "user", "content": user_prompt}
    )

    # Keep the system instruction separate from stored chat history
    messages = [
        {"role": "system", "content": "You are a helpful assistant"},
        *st.session_state.chat_history,
    ]

    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Thinking..."):
            response = llm.invoke(messages)

        assistant_response = response.content
        st.markdown(assistant_response)

    st.session_state.chat_history.append(
        {"role": "assistant", "content": assistant_response}
    )

