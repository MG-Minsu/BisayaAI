import streamlit as st
from openai import OpenAI
from openai import AsyncOpenAI
import asyncio

# Set the API key using Streamlit's secrets management
client = AsyncOpenAI(
    api_key=st.secrets["API_key"],
)


async def bisaya_chatbot_response(user_input):
    try:
        # Constructing a prompt for a chatbot that replies in Bisaya
        prompt_text = f"Assume you are a chatbot fluent in Bisaya. An English speaker is talking to you, and you need to reply in Bisaya. Here's the conversation:\n\nEnglish: {user_input}\nBisaya:"
        
        # Correct API call using the latest API version
        response = await client.chat.completions.create(
            model="gpt-3.5-turbo", 
            messages=[
                {"role": "system", "content": "You are a chatbot that converses in Bisaya."},
                {"role": "user", "content": user_input}
            ],# Using a suitable model for chat-like interactions
            prompt=prompt_text,
            max_tokens=100,
            temperature=0.9,
            stop=["\n", " English:", " Bisaya:"]
        )
        return response.choices[0].text.strip()  # Correcting the key from 'text' to match the API response structure
    except Exception as e:
        return f"Error: {str(e)}"

async def main():
    st.title('Bisaya Speaking Chatbot')
    user_input = st.text_input("Type in English and the chatbot will reply in Bisaya:")
    
    if st.button("Send"):
        # Run the chatbot response generation asynchronously
        response = await bisaya_chatbot_response(user_input)
        st.text_area("Chatbot says (in Bisaya):", value=response, height=200)

if __name__ == "__main__":
    # Run the Streamlit app asynchronously
    asyncio.run(main())
