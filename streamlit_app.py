import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
import openai
openai.api_key = st.secrets["API_key"]
import hashlib


openai.api_key = st.secrets["API_key"]


def bisaya_chatbot_response(user_input):
    try:
        # Constructing a prompt for a chatbot that replies in Bisaya
        prompt_text = f"Assume you are a chatbot fluent in Bisaya. An English speaker is talking to you, and you need to reply in Bisaya. Here's the conversation:\n\nEnglish: {user_input}\nBisaya:"
        
        # OpenAI API call updated for API version 1.0.0+
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use the most appropriate model available
            messages=[
                {"role": "system", "content": "You are a chatbot that converses in Bisaya."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=150,
            temperature=0.9,
            stop=["\n", " English:", " Bisaya:"]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    st.title('Bisaya Speaking Chatbot')
    user_input = st.text_input("Type in English and the chatbot will reply in Bisaya:")
    
    if st.button("Send"):
        reply = bisaya_chatbot_response(user_input)
        st.text_area("Chatbot says (in Bisaya):", value=reply, height=200)

if __name__ == "__main__":
    main()
