"""
Rathinam College AI Assistant — Streamlit App
General Helpdesk for all Students
"""

import os
import sys

# Add project root to path so imports work
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from groq import Groq

from data.college_data import KNOWLEDGE_BASE
from app.retriever import RAGRetriever

# ── Config ──────────────────────────────────────────────────────────────────
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
MODEL = "llama-3.1-8b-instant"

SYSTEM_PROMPT = """You are a helpful and professional AI Assistant for Rathinam College, Coimbatore. 

You provide accurate information about ALL aspects of the college, including Engineering, Arts & Science, Admissions, PG courses, and Fees.

CRITICAL INSTRUCTIONS:
1. Use the [title] in the context to understand the meaning of the user's quest.
2. If the user asks for "Undergraduate" or "UG", look for Bachelors programs. If they ask for "Postgraduate" or "PG", look for Masters programs.
3. ALWAYS provide the specific information (like fee amounts or course lists) found in the context. 
4. NEVER suggest searching a portal or website. 
5. NEVER include keywords, IDs, or technical metadata in your response.
6. If the information is not in the context, say: "I don't have that specific information in my current database."

Be concise and maintain a professional "College Helpdesk" tone.

CONTEXT:
{context}
"""

# ── Initialize retriever (cached so it's built only once) ────────────────────
@st.cache_resource
def get_retriever():
    return RAGRetriever(KNOWLEDGE_BASE)

retriever = get_retriever()

# ── Initialize Groq client ──────────────────────────────────────────────────
@st.cache_resource
def get_groq_client():
    return Groq(api_key=GROQ_API_KEY)

client = get_groq_client()

# ── Page config ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Rathinam College AI Assistant",
    page_icon="🎓",
    layout="centered",
)

# ── Custom CSS ──
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@300;400;500&display=swap');

    /* Global */
    .stApp {
        background-color: #FAFAF8;
        font-family: 'DM Sans', sans-serif;
    }

    /* Main Container Padding */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 5rem !important;
    }

    /* Header styling */
    .header-container {
        background: #7B1D1D;
        color: white;
        padding: 0.8rem 1.5rem;
        display: flex;
        align-items: center;
        gap: 14px;
        border-bottom: 3px solid #C9962E;
        border-radius: 12px 12px 0 0;
        margin-bottom: 1rem;
    }
    .logo-circle {
        width: 44px; height: 44px;
        background: #C9962E;
        border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        font-family: 'DM Serif Display', serif;
        font-size: 20px;
        color: #7B1D1D;
        font-weight: bold;
        flex-shrink: 0;
    }
    .header-text h1 {
        font-family: 'DM Serif Display', serif !important;
        font-size: 1.3rem !important;
        font-weight: 400 !important;
        margin: 0 !important;
        color: white !important;
        letter-spacing: 0.01em;
        line-height: 1.2 !important;
    }
    .header-text p {
        font-size: 0.75rem !important;
        opacity: 0.85;
        margin: 0 !important;
    }

    /* Status badge */
    .status-dot {
        margin-left: auto;
        display: flex; align-items: center; gap: 8px;
        font-size: 0.75rem;
        opacity: 0.9;
    }
    .dot { width: 8px; height: 8px; border-radius: 50%; background: #4ade80; }

    /* Chat messages */
    .stChatMessage {
        background-color: transparent !important;
        padding: 0.5rem 0 !important;
    }
    
    /* User Chat Bubble */
    [data-testid="stChatMessage"]:nth-child(even) > div:nth-child(2) {
        background-color: #7B1D1D !important;
        color: white !important;
        border-radius: 16px !important;
        border-top-right-radius: 4px !important;
    }

    /* Assistant Chat Bubble */
    [data-testid="stChatMessage"]:nth-child(odd) > div:nth-child(2) {
        background-color: #FFFFFF !important;
        color: #1A1A1A !important;
        border-radius: 16px !important;
        border-top-left-radius: 4px !important;
        border: 1px solid #E5E0D8 !important;
    }

    /* Chat container spacing */
    [data-testid="stChatMessageContainer"] {
        gap: 1.2rem !important;
    }

    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Input focus */
    .stChatInputContainer textarea:focus {
        border-color: #7B1D1D !important;
    }
</style>
""", unsafe_allow_html=True)

# ── Header ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="header-container">
    <div class="logo-circle">R</div>
    <div class="header-text">
        <h1>Rathinam College Assistant</h1>
        <p>Official College Helpdesk</p>
    </div>
    <div class="status-dot"><div class="dot"></div> Online</div>
</div>
""", unsafe_allow_html=True)

# ── Session state for chat history ──────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "👋 Hello! I'm the Rathinam College AI Assistant. "
                "Ask me about courses, campus life, admissions, placements, and more!"
            ),
        }
    ]

# ── Display existing messages ───────────────────────────────────────────────
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ── Chat input ──────────────────────────────────────────────────────────────
if user_input := st.chat_input("Ask about Rathinam College..."):
    # Validate API key
    if not GROQ_API_KEY:
        st.error("⚠️ GROQ_API_KEY is not set. Please add it to your `.env` file.")
        st.stop()

    # Display user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            # 1. Retrieve relevant context (Top K for broad coverage)
            context = retriever.build_context(user_input, top_k=8)

            # 2. Build prompt
            prompt = SYSTEM_PROMPT.format(context=context) + f"\n\nUser Question: {user_input}"

            try:
                # 3. Call Groq API
                response = client.chat.completions.create(
                    model=MODEL,
                    messages=[{"role": "user", "content": prompt}],
                )
                reply = response.choices[0].message.content
            except Exception as e:
                reply = f"❌ Error communicating with the AI model: {str(e)}"

        # Display reply (Sources removed as requested)
        st.markdown(reply)

    # Save to session state
    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )
