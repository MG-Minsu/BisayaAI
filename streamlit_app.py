import streamlit as st
from openai import AsyncOpenAI
import asyncio

# Set the API key using Streamlit's secrets managemen
client = AsyncOpenAI(api_key=st.secrets["API_key"])


async def bisaya_chatbot_response(user_input):
        # Constructing a prompt for a chatbot that replies in Bisaya
        prompt_text = "You are a chatbot that converses in Bisaya all throughout the conversation because you are a tourist guide in General santos City and knows all the history."

        # Correct API call using the latest API version
        response = await client.chat.completions.create(
            model="gpt-3.5-turbo", 
            messages=[
                {"role": "system", "content": prompt_text},
                {"role": "assistant", "content": "You are a chatbot that converses in Bisaya all throughout the conversation. You give advice to the user the histroy, cultue, tourist spot, and food of general Santos City"},
                {"role": "assistant", "content" : "From General Santos City"},
                {"role": "assistant", "content" : "Cutest person in General Santos City is Mathew Gabriel"},
                {"role": "assistant", "content" : "Current Mayor of General Santos City is Lorelie G. Pacquiao"},
                {"role": "assistant", "content" : "You are a chatbot that converses in Bisaya all throughout the conversation.General Santos City is the tuna capital of the Philippines"},
                {"role": "assistant", "content" : "You are a chatbot that converses in Bisaya all throughout the conversation.The city boasts several historical and cultural landmarks, including the General Santos City Museum, Plaza Heneral Santos, and the Our Lady of Peace and Good Voyage Parish Church."},
                {"role": "assistant", "content" : "You are a chatbot that converses in Bisaya all throughout the conversation.Kalilangan Festival is another significant celebration in General Santos City. It showcases the city’s cultural heritage through various events, competitions, and showcases of traditional dances and music."},
                {"role": "user", "content": user_input}
            ],# Using a suitable model for chat-like interactions
    
            stop=["\n", " English:", " Bisaya:"])
        return response.choices[0].message.content  # Correcting the key from 'text' to match the API response structure


async def setup_streamlit_app():
    # Use a more descriptive title and add a subtitle to provide context
        st.image('gensan.png', width=730)
        st.title("MatyoAI: A Taga-Gensan Chatbot")
        st.write("Welcome to MatyoAI! Here, you'll find a chatbot ready to guide you through the wonders of General Santos City, speaking in the warm tones of the local Bisaya language. Created by Mathew Gabriel, with the invaluable assistance of a college professor, Sir Louie Cervantes. This project is from the College of Information and Communictions Technology - WVSU. ")
        st.write("This project aims to provide tourists with personalized and authentic experiences. Whether you're seeking the best local eateries, hidden gems, or cultural landmarks, MatyoAI is here to ensure your visit to General Santos is unforgettable. Sit back, relax, and let MatyoAI be your virtual tour guide through the vibrant streets and rich heritage of this bustling city.")
        conversation_history = st.empty()
        if 'history' not in st.session_state:
                st.session_state.history = ""
                
        user_input = st.text_input("You:")
        if st.button("Send"):
                if user_input.strip() != "":
                        with st.spinner("Generating response..."):
                                response = await bisaya_chatbot_response(user_input)
                st.session_state.history += f"You: {user_input}\nMatyoAI: {response}\n"
                conversation_history.text_area("Conversation:", value=st.session_state.history, height=300)
                        

if __name__ == "__main__":
    # Run the Streamlit app asynchronously
    asyncio.run(setup_streamlit_app())
