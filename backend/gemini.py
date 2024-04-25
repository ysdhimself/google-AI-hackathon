import requests
from dotenv import load_dotenv
import google.generativeai as genai
import os


# Function to load environment variables from .env file
def configure():
    load_dotenv()


class Porter:
    def __init__(self):
        self.chat_history = []
        self.prompt = """
        You are a virtual personal assistant name "porter" tasked with managing email communications. Upon receiving an email:
        1.Summarize the email contents succinctly.
        2.Relay the summary to the user and request their input for any response.
        3.Based on the user's instructions or a brief response, draft a comprehensive reply.
        4.Send the finalized email response.
        Ensure to maintain a polite tone throughout the communications and handle all data with confidentiality.
        """
        # Load environment variables
        configure()
        # Configure the generative AI with the API key from environment variables
        genai.configure(api_key=os.getenv('api_key'))

        # Set up the model configuration
        self.generation_config = {
            "temperature": 0.9,
            "top_p": 1,
            "top_k": 1,
            "max_output_tokens": 2048,
        }

        # Set up the safety settings for the model
        self.safety_settings = [
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
        self.model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                                           generation_config=self.generation_config,
                                           safety_settings=self.safety_settings,
                                           system_instruction=self.prompt)

    def sum_received_email(self, chat):
        # Start a chat with the model
        convo = self.model.start_chat(history=[])

        # Send a message to the model and print the model's response
        convo.send_message(f"summarize this email: {chat}")
        result = convo.last.text
        print(result)
        self.chat_history.append(result)

    def user_reply_email(self, chat):
        convo = self.model.start_chat(history=[])

        # Send a message to the model and print the model's response
        convo.send_message(f"generate email from this user answer: {chat}")
        result = convo.last.text
        print(result)
        self.chat_history.append(result)

    def print_chat_history(self):
        print(self.chat_history)


# Main function to run the application
def main():
    porter = Porter()
    print("NUMBER 1")
    porter.sum_received_email(chat="hello Hafiz I want to make appointment with you")
    print("NUMBER 2")
    porter.user_reply_email(chat="sure let's make appointment. I will available this monday let me know what time you available")
    print("NUMBER 3")
    porter.sum_received_email(chat="I will available 11 AM")

    porter.print_chat_history()


# Run the main function if the script is run directly
if __name__ == '__main__':
    main()
