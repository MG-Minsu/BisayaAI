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
        st.title("ChatGPT")
        
            conversation_history = st.empty()
            user_input = st.text_input("You:")
            if st.button("Send"):
                if user_input.strip() != "":
                    with st.spinner("Generating response..."):
                        response = generate_response(user_input)
                    conversation_history.text_area("Conversation:", value=f"You: {user_input}\nChatGPT: {response}\n", height=300)
                

if __name__ == "__main__":
    # Run the Streamlit app asynchronously
    asyncio.run(setup_streamlit_app())
