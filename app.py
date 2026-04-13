import streamlit as st
from funny_chatbot import generate_joke

st.set_page_config(
    page_title="Funny Chatbot - AI Humor Generator",
    page_icon="😂",
    layout="centered"
)

st.title("😂 Funny Chatbot")
st.subheader("AI Humor Generator")
st.write("Enter any topic and I'll tell you a joke about it!")

# User input
user_input = st.text_input(
    "Enter a topic:",
    placeholder="e.g., cars, programming, cats...",
    help="Type anything you want a joke about!"
)

# Generate button with loading state
if st.button("🎭 Generate Joke", type="primary"):
    if user_input:
        with st.spinner("Making something funny..."):
            joke = generate_joke(user_input)
            st.success(joke)
    else:
        st.warning("⚠️ Please enter a topic first!")


st.write("Finished testing? Help us improve:")
st.link_button("Submit Feedback Survey", "https://forms.gle/cEtWBGpYU2dvQA8H8")

# Add some fun footer
st.markdown("---")
st.markdown("*Powered by Adli Amin*")
