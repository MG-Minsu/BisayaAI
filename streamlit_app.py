import streamlit as st
from openai import OpenAI
from openai import AsyncOpenAI

# Set the API key using Streamlit's secrets management
client = AsyncOpenAI(
    api_key=st.secrets["API_key"],
)

async def bisaya_chatbot_response(user_input):
    try:
        # Constructing a prompt for a chatbot that replies in Bisaya
        prompt_text = f"Assume you are a chatbot fluent in Bisaya. An English speaker is talking to you, and you need to reply in Bisaya. Here's the conversation:\n\nEnglish: {user_input}\nBisaya:"
        
        # Correct API call using the latest API version
        response = openai.chat.completions.create(
            model="GPT-3.5-turbo-0125",  # Assuming using a suitable model for chat-like interactions
            prompt=prompt_text,
            max_tokens=100,
            temperature=0.9,
            stop=["\n", " English:", " Bisaya:"]
        )
        return response.choices[0].text.strip()  # Correcting the key from 'text' to match the API response structure
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
