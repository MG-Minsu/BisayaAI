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
        st.subheader('Type in English and get a response in Bisaya')
        
        # Create a text area to display the conversation history
        conversation_history = st.text_area('Conversation History:', height=300, disabled=True)
        
        # Use a conditional statement to handle the button click event
        if 'conversation' not in st.session_state:
            st.session_state.conversation = []
        
        # Use a more intuitive variable name and add a placeholder for user input
        user_message = st.text_input('Enter your message...', placeholder='Type here...', key='user_input')
        
        # Use a more descriptive button label and add some space around it
        send_button = st.button('Send Message', key='send_button')
        
        # Use a conditional statement to handle the button click event
        if send_button:
            # Use a try-except block to handle any errors that may occur
            try:
                chatbot_response = await bisaya_chatbot_response(user_message)
                # Update the conversation history
                st.session_state.conversation.append(f'**You:** {user_message}')
                st.session_state.conversation.append(f'**MatyoAI:** {chatbot_response}')
                conversation_history.value = '\n\n'.join(st.session_state.conversation)
            except Exception as e:
                st.error(f'Error: {e}')


if __name__ == "__main__":
    # Run the Streamlit app asynchronously
    asyncio.run(setup_streamlit_app())
