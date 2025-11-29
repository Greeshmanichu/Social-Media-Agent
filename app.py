import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
import pandas as pd
from datetime import datetime, timedelta

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# ---------------------- PAGE CONFIG ----------------------
st.set_page_config(
    page_title="AI Social Media Agent",
    page_icon="✨",
    layout="wide"
)

# ---------------------- CUSTOM CSS (Gradient + Glass UI) ----------------------
gradient_css = """
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* Gradient Background */
.stApp {
    background: linear-gradient(135deg, #6d5dfc 0%, #c89bff 50%, #ff87d6 100%);
    background-size: cover;
}

/* Glass Card */
.glass-card {
    background: rgba(255, 255, 255, 0.16);
    border-radius: 20px;
    padding: 25px;
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.25);
    box-shadow: 0px 4px 30px rgba(0,0,0,0.1);
}

/* Title */
.big-title {
    font-size: 45px;
    font-weight: 700;
    text-align: center;
    background: -webkit-linear-gradient(#ffffff, #ffe1ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Subtitle */
.sub-text {
    font-size: 18px;
    text-align: center;
    color: #fff;
    opacity: 0.9;
    margin-top: -15px;
}

/* Neon Button */
.stButton>button {
    background: linear-gradient(135deg, #ff8af0, #8a5bff);
    color: white;
    padding: 12px 30px;
    border-radius: 12px;
    font-weight: 600;
    border: none;
    transition: 0.2s;
}

.stButton>button:hover {
    transform: scale(1.05);
    background: linear-gradient(135deg, #8a5bff, #ff8af0);
}

</style>
"""
st.markdown(gradient_css, unsafe_allow_html=True)

# ---------------------- HEADER ----------------------
st.markdown("<h1 class='big-title'>✨ AI Social Media Agent</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-text'>Generate creative content, captions & posting plans — beautifully.</p>", unsafe_allow_html=True)

st.write("") 
st.write("")

# ---------------------- MAIN FORM ----------------------
with st.container():
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)

    col1, col2 = st.columns([2,1])

    with col1:
        brand = st.text_input("Brand / Topic", placeholder="Ex: Eco-friendly water bottle")
        description = st.text_area("About the brand / USP", placeholder="Describe the product in 1–2 lines...")
        audience = st.text_input("Target Audience", placeholder="Ex: Students, professionals")
        examples = st.text_area("Sample style (optional)")

    with col2:
        platform = st.selectbox("Platform", ["Instagram", "Twitter", "LinkedIn", "Facebook", "TikTok"])
        tone = st.selectbox("Tone", ["Casual", "Professional", "Playful", "Inspirational"])
        num_posts = st.slider("Number of posts", 1, 10, 5)
        include_hashtags = st.checkbox("Include Hashtags", True)
        schedule_days = st.number_input("Schedule (N days)", 0, 30, 7)

    submitted = st.button("✨ Generate Content")

    st.markdown("</div>", unsafe_allow_html=True)


# ---------------------- PROMPT ----------------------
# ---------------------- PROMPT ----------------------
def build_prompt():
    prompt = f"""
Generate {num_posts} Instagram-style flashcards for {brand} / {platform}.

Brand: {brand}
Description: {description}
Audience: {audience}
Tone: {tone}

For each flashcard, include:
- Title (short & catchy)
- Caption (short, engaging)
- Background / Image suggestion (for Instagram visual)
- Emoji or visual cues to make it pop

Output FORMAT:
Return as **plain text**, not strict JSON.
Number each flashcard.
Example:

Flashcard 1:
Title: "..."
Caption: "..."
Image suggestion: "..."
Emoji/Visual: "..."

"""
    if examples:
        prompt += f"\nMatch style: {examples}"
    return prompt


# ---------------------- GEMINI API ----------------------
def call_gemini(prompt):
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        st.error(f"Gemini Error: {e}")
        return None


# ---------------------- GENERATION LOGIC ----------------------
# ---------------------- GENERATION LOGIC ----------------------
if submitted:
    if not brand:
        st.error("Please enter a brand name to continue.")
        st.stop()

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)

    with st.spinner("✨ Creating Instagram-style flashcards..."):
        raw = call_gemini(build_prompt())

    if raw:
        st.subheader("🎨 Generated Instagram Flashcards")
        # Display as plain text flashcards
        st.text_area("Flashcards Output", raw, height=500)
        
        # Optionally: split by "Flashcard X" to create individual sections
        flashcards = [f.strip() for f in raw.split("Flashcard") if f.strip()]
        for f in flashcards:
            st.markdown(f"### Flashcard {f.splitlines()[0]}")
            for line in f.splitlines()[1:]:
                st.markdown(line)

    st.markdown("</div>", unsafe_allow_html=True)
