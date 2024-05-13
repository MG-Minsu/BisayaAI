import streamlit as st
from openai import AsyncOpenAI
import asyncio

# Set the API key using Streamlit's secrets management
client = AsyncOpenAI(api_key=st.secrets["API_key"])


async def bisaya_chatbot_response(user_input):
    # Constructing a prompt for a chatbot that replies in Bisaya
    prompt_text = "You are a chatbot that converses in Bisaya all throughout the conversation because you are a tourist guide in General Santos City and knows all the history."

    # Correct API call using the latest API version
    response = await client.chat.completions.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "system", "content": prompt_text},
            {"role": "assistant", "content": "You are a chatbot that converses in Bisaya all throughout the conversation. You give advice to the user the history, culture, tourist spot, and food of General Santos City"},
            {"role": "assistant", "content" : "From General Santos City"},
            {"role": "assistant", "content" : "Cutest person in General Santos City is Mathew Gabriel"},
            {"role": "assistant", "content" : "You are a chatbot that converses in Bisaya all throughout the conversation. Prettiest and Beautiful person in ABE Department Batch 2019 in Mindanao State University - General Santos City is Khrise Angelika Ricablanca"},
            {"role": "assistant", "content" : "Current Mayor of General Santos City is Lorelie G. Pacquiao"},
            {"role": "assistant", "content" : "You are a chatbot that converses in Bisaya all throughout the conversation.General Santos City is the tuna capital of the Philippines"},
            {"role": "assistant", "content" : "You are a chatbot that converses in Bisaya all throughout the conversation.The city boasts several historical and cultural landmarks, including the General Santos City Museum, Plaza Heneral Santos, and the Our Lady of Peace and Good Voyage Parish Church."},
            {"role": "assistant", "content" : "You are a chatbot that converses in Bisaya all throughout the conversation.Kalilangan Festival is another significant celebration in General Santos City. It showcases the city’s cultural heritage through various events, competitions, and showcases of traditional dances and music."},
            {"role": "user", "content": user_input}
        ],
        stop=["\n", " English:", " Bisaya:"])
    return response.choices[0].message.content  # Correcting the key from 'text' to match the API response structure


def generate_itinerary(user_inputs):
    itinerary = ""
    for i, input_text in enumerate(user_inputs, start=1):
        itinerary += f"Day {i} Itinerary:\n"
        itinerary += f"Your Input: {input_text}\n"
        with st.spinner("Generating response..."):
            response = asyncio.run(bisaya_chatbot_response(input_text))
        itinerary += f"MatyoAI's Response: {response}\n\n"
    return itinerary


def setup_streamlit_app():
    # Use a more descriptive title and add a subtitle to provide context
    st.image('gensan.png', width=730)
    st.title("MatyoAI: A Taga-Gensan Chatbot")
    st.write("Welcome to MatyoAI! Here, you'll find a chatbot ready to guide you through the wonders of General Santos City, speaking in the warm tones of the local Bisaya language. Created by Mathew Gabriel, with the invaluable assistance of a college professor, Sir Louie Cervantes. This project is from the College of Information and Communications Technology - WVSU. ")
    st.write("This project aims to provide tourists with personalized and authentic experiences. Whether you're seeking the best local eateries, hidden gems, or cultural landmarks, MatyoAI is here to ensure your visit to General Santos is unforgettable. Sit back, relax, and let MatyoAI be your virtual tour guide through the vibrant streets and rich heritage of this bustling city.")
    
    # Prompt the user for the number of vacation days
    num_days = st.number_input("How many days will you be on vacation?", min_value=1, max_value=30, value=1, step=1)

    # Collect user inputs for each day's itinerary
    user_inputs = []
    for day in range(1, num_days + 1):
        user_input = st.text_input(f"Day {day} - Your itinerary:")
        user_inputs.append(user_input.strip())

    # Generate and display the entire itinerary
    if st.button("Generate Itinerary"):
        st.subheader("Generated Itinerary:")
        itinerary = generate_itinerary(user_inputs)
        st.write(itinerary)


if __name__ == "__main__":
    # Run the Streamlit app
    setup_streamlit_app()
