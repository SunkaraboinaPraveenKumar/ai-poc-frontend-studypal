import streamlit as st
import requests

# Page Configuration
st.set_page_config(
    page_title="StudyPal",
    page_icon="🤖",
    layout="centered"
)

st.title("📚 StudyPal Application")

API_URL = "http://127.0.0.1:8000/ask"

# Supported Providers & Models
PROVIDERS = ["Groq", "Ollama", "Gemini"]
GROQ_MODELS = ["gemma2-9b-it", "llama-3.1-8b-instant", "llama-3.3-70b-versatile"]
OLLAMA_MODELS = ["gemma:2b", "phi", "deepseek-r1-1.5b"]
GOOGLE_MODELS = ["gemini-2.5-flash-preview-04-17", "gemini-2.0-flash", "gemini-2.0-flash-exp-image-generation", "gemini-1.5-pro"]

# Initialize Session State
st.session_state.setdefault("show_settings", False)
st.session_state.setdefault("provider", PROVIDERS[0])
st.session_state.setdefault("model", GROQ_MODELS[0])

col1, col2 = st.columns([8, 1])
user_question = col1.text_input(label="Ask Your Question", placeholder="eg. What is AI?")

if col2.button("⚙️", help="Select Model Settings"):
    st.session_state.show_settings = not st.session_state.show_settings

if st.session_state.show_settings:
    with st.expander("🔧 Model Settings", expanded=True):
        # Provider selection
        st.session_state.provider = st.selectbox(
            label="Provider", options=PROVIDERS,
            index=PROVIDERS.index(st.session_state.provider)
        )
        # Adjust model options based on provider
        if st.session_state.provider == "Groq":
            models = GROQ_MODELS
        elif st.session_state.provider == "Ollama":
            models = OLLAMA_MODELS
        else:
            models = GOOGLE_MODELS
        st.session_state.model = st.selectbox(
            label="Model", options=models,
            index=models.index(st.session_state.model) if st.session_state.model in models else 0
        )
        st.success(f"Using {st.session_state.provider} - {st.session_state.model}")

# Get Answer from API
if st.button("Get Answer"):
    response = requests.post(
        url=API_URL,
        json={'question': cuser_question}
    )
    result = response.json()
    answer = result["answer"]
    st.success(answer)