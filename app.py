import streamlit as st
from funny_chatbot import generate_joke

st.title("😂 Funny Chatbot – AI Humor Generator")
st.write("Ask the AI to tell a joke about anything!")

user_input = st.text_input("Enter a topic:")
if st.button("Generate Joke"):
    if user_input:
        joke = generate_joke(f"Tell a funny joke about {user_input}.")
        st.success(joke)
    else:
        st.warning("Please enter a topic first!")
