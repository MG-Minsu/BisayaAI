import streamlit as st
from openai import AsyncOpenAI
import asyncio

# Set the API key using Streamlit's secrets management
openai_client = AsyncOpenAI(api_key=st.secrets["API_key"])


async def generate_chatbot_response(user_input):
    try:
        prompt_text = f"Assume you are a chatbot fluent in Bisaya. An English speaker is talking to you, and you need to reply in Bisaya. Here's the conversation:\n\nEnglish: {user_input}\nBisaya:"
        response = await openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a chatbot that converses in Bisaya."},
                {"role": "user", "content": user_input}
            ],
            stop=["\n", " English:", " Bisaya:"]
        )
        return response.choices[0].messages[0].content
    except OpenAIError as e:
        return f"Error: {str(e)}"


async def setup_streamlit_app():
    st.title('Bisaya Speaking Chatbot')
    user_input = st.text_input("Type in English and the chatbot will reply in Bisaya:")
    send_button = st.button("Send")

    if send_button:
        chatbot_response = await generate_chatbot_response(user_input)
        st.text_area("Chatbot says (in Bisaya):", value=chatbot_response, height=200)


if __name__ == "__main__":
    # Run the Streamlit app asynchronously
    asyncio.run(setup_streamlit_app())
