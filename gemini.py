import requests
from dotenv import load_dotenv
import google.generativeai as genai
import os

# Function to load environment variables from .env file
def configure():
    load_dotenv()

# Main function to run the application
def main():
    # Load environment variables
    configure()
    # Configure the generative AI with the API key from environment variables
    genai.configure(api_key=os.getenv('api_key'))

    # Set up the model configuration
    generation_config = {
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
    }

    # Set up the safety settings for the model
    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
    ]

    # Initialize the generative model with the specified configuration and safety settings
    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                  generation_config=generation_config,
                                  safety_settings=safety_settings)

    # Start a chat with the model
    convo = model.start_chat(history=[])

    # Send a message to the model and print the model's response
    convo.send_message("tell me about canada")
    print(convo.last.text)

# Run the main function if the script is run directly
if __name__ == '__main__':
    main()