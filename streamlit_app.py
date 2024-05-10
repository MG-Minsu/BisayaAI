import streamlit as st
from openai import AsyncOpenAI
import asyncio

# Set the API key using Streamlit's secrets managemen
client = AsyncOpenAI(api_key=st.secrets["API_key"])


async def bisaya_chatbot_response(user_input):
        # Constructing a prompt for a chatbot that replies in Bisaya
        prompt_text = "You are a chatbot that converses in Bisaya all throughout the conversation."

        # Correct API call using the latest API version
        response = await client.chat.completions.create(
            model="gpt-3.5-turbo", 
            messages=[
                {"role": "system", "content": prompt_text},
                {"role": "assistant", "content" : "From General Santos City"},
                {"role": "user", "content": user_input}
            ],# Using a suitable model for chat-like interactions
    
            stop=["\n", " English:", " Bisaya:"])
        return response.choices[0].message.content  # Correcting the key from 'text' to match the API response structure


async def setup_streamlit_app():
    # Use a more descriptive title and add a subtitle to provide context
        st.title('Bisaya Speaking Chatbot') 
        user_input = st.text_input("Type in English and the chatbot will reply in Bisaya:") 
        send_button = st.button("Send")

        if send_button:
            chatbot_response = await bisaya_chatbot_response(user_input)
            st.text_area("Chatbot says (in Bisaya):", value=chatbot_response)
                

if __name__ == "__main__":
    # Run the Streamlit app asynchronously
    asyncio.run(setup_streamlit_app())
