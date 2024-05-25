# MatyoAI: A Taga-Gensan Chatbot

Welcome to MatyoAI! This chatbot is designed to guide you through the wonders of General Santos City, speaking in the warm tones of the local Bisaya language. Created by Mathew Gabriel, with the invaluable assistance of a college professor, Sir Louie Cervantes. This project is from the College of Information and Communications Technology - WVSU.

## Overview

MatyoAI provides tourists with personalized and authentic experiences in General Santos City. Whether you're seeking the best local eateries, hidden gems, or cultural landmarks, MatyoAI is here to ensure your visit is unforgettable.

## Features

- **Bisaya Chatbot**: Interact with a chatbot that converses in Bisaya.
- **Tourist Guide**: Get recommendations for places to visit in General Santos City.
- **Itinerary Generator**: Generate a custom itinerary for your vacation.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/matyoai.git
    ```
2. Navigate to the project directory:
    ```bash
    cd matyoai
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
4. Set up Streamlit's secrets management to include your OpenAI API key. Create a `.streamlit` directory and a `secrets.toml` file within it:
    ```plaintext
    [secrets]
    API_key = "your_openai_api_key"
    ```

## Usage

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. Navigate to the local server URL provided by Streamlit.

## Navigating the App

### Home Page

- **Welcome Message**: Introduction to MatyoAI and its purpose.
- **Image and Title**: Visual introduction with an image of General Santos City.

### Chat Interface

- **Text Input**: Enter your messages here to converse with MatyoAI.
- **Send Button**: Click to send your message.
- **Conversation History**: View the ongoing conversation.

### Itinerary Generation

- **Vacation Days Input**: Enter the number of days for your vacation.
- **Generate Itinerary Button**: Click to generate a custom itinerary based on the number of days you specified.
- **Generated Itinerary**: View the suggested itinerary for your trip.

## Contributing

We welcome contributions! Please fork the repository and submit pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Mathew Gabriel
- Sir Louie Cervantes
- College of Information and Communications Technology - WVSU

Enjoy your virtual tour of General Santos City with MatyoAI!

