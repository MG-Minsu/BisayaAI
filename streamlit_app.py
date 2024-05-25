import streamlit as st
from openai import AsyncOpenAI
import asyncio
from datetime import datetime, timedelta

# Set the API key using Streamlit's secrets management
client = AsyncOpenAI(api_key=st.secrets["API_key"])

# Places to visit in General Santos City
places_to_visit = [
    "Plaza Heneral Santos",
    "General Santos City Museum",
    "Our Lady of Peace and Good Voyage Parish Church",
    "T'boli Weaving Center",
    "Tuna Auction Market",
    "Fish Port Complex",
    "Queen Tuna Park",
    "Sanchez Peak",
    "Balut Island",
    "Isabela City",
    "Sun City Suites",
    "Lemlunay Resort",
    "Island Buenavista",
    "Pioneer Avenue",
    "St. Paul Novitiate Park",
    "General Santos City Hall"
]

async def guide_chatbot_response(user_input):
    # Constructing a prompt for a chatbot that replies in Bisaya
    prompt_text = "You speak Bisaya. You provide itinerary per day in General Santos City, including a description of each place."

    response = await client.chat.completions.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "system", "content": prompt_text},
            {"role": "user", "content": user_input}
        ],
        stop=["\n", " English:", " Bisaya:"])
    return response.choices[0].message.content 

# Iterate through places_to_visit list in order without random selection
async def generate_itinerary(dates):
    itinerary = ""
    for i, date in enumerate(dates):
        place_to_visit = places_to_visit[i % len(places_to_visit)]  # Loop through the places list
        user_input = f"On {date}, I will visit {place_to_visit}. Can you provide a description of this place?"
        with st.spinner("Generating itinerary..."):
            response = await guide_chatbot_response(user_input)
        itinerary += f"**Itinerary for {date}:**<br>"
        itinerary += f"**Place:** {place_to_visit}<br>"
        itinerary += f"**Description:**<br>{response}<br><br>"
    return itinerary

def setup_streamlit_app():

    st.image('gensan.png', width=730)
    st.title("MatyoAI: A Taga-Gensan Chatbot")
    st.write("Welcome to MatyoAI! Here, you'll find a chatbot ready to guide you through the wonders of General Santos City, speaking in the warm tones of the local Bisaya language. Created by Mathew Gabriel, with the invaluable assistance of a college professor, Sir Louie Cervantes. This project is from the College of Information and Communications Technology - WVSU. ")
    st.write("This project aims to provide tourists with personalized and authentic experiences. Whether you're seeking the best local eateries, hidden gems, or cultural landmarks, MatyoAI is here to ensure your visit to General Santos is unforgettable. Sit back, relax, and let MatyoAI be your virtual tour guide through the vibrant streets and rich heritage of this bustling city.")
    
    # Conversation history
    conversation_history = st.empty()
    if 'history' not in st.session_state:
        st.session_state.history = ""

    # Chat interface
    user_input = st.text_input("You:")
    if st.button("Send"):
        if user_input.strip() != "":
            with st.spinner("Generating response..."):
                response = asyncio.run(bisaya_chatbot_response(user_input))
            st.session_state.history += f"You: {user_input}\nMatyoAI: {response}\n"
            conversation_history.text_area("Conversation:", value=st.session_state.history, height=300)

    # Prompt the user to select vacation dates
    start_date = st.date_input("Select start date of your vacation")
    num_days = st.number_input("How many days will you be on vacation?", min_value=1, max_value=30, value=1, step=1)

    # Generate the list of dates for the itinerary
    vacation_dates = [start_date + timedelta(days=i) for i in range(num_days)]

    # Generate and display the entire itinerary
    if st.button("Generate Itinerary"):
        itinerary = asyncio.run(generate_itinerary(vacation_dates))
        st.subheader("Generated Itinerary:")
        st.markdown(itinerary, unsafe_allow_html=True)

async def bisaya_chatbot_response(user_input):
    # Constructing a prompt for a chatbot that focuses on generating the itinerary list only
    prompt_text = "You are a chatbot that converses in Bisaya and focuses on generating an itinerary list for General Santos City. Provide detailed descriptions for each place."

    response = await client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt_text},
            {"role": "user", "content": user_input}
        ],
        stop=["\n", " English:", " Bisaya:"])
    return response.choices[0].message.content  

if __name__ == "__main__":
    # Run the Streamlit app
    setup_streamlit_app()
