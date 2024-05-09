import streamlit as st
import openai

# Set your OpenAI API key here
#openai.api_key = 'your-openai-api-key'
openai.api_key = st.secrets["API_key"]
def translate_to_bisaya(text):
    try:
        # This is a placeholder for the actual OpenAI API call
        response = openai.Completion.create(
            engine="text-davinci-003",  # Replace with the suitable engine
            prompt=f"Translate English to Bisaya: {text}",
            max_tokens=60
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    st.title('English to Bisaya Translator')
    user_input = st.text_input("Enter English text:")
    if st.button("Translate"):
        translation = translate_to_bisaya(user_input)
        st.text_area("Translated Text", value=translation, height=200)

if __name__ == "__main__":
    main()
