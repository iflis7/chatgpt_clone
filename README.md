# ChatGPT Clone "Bart Version"

This project uses the OpenAI API and Gradio to build a chatbot that can carry on a conversation with a user. The chatbot is based on the character Bart Simpson from The Simpsons and is designed to have a mischievous and rebellious personality.

## Running the Chatbot

To run the chatbot, clone this repository and install the required dependencies:

### pip install openai gradio
You will also need to sign up for an API key from OpenAI and set it as an environment variable named `OPENAI_KEY`.

Finally, run the `main.py` file to launch the chatbot:

### python main.py

## Using the Chatbot

To start a conversation with the chatbot, type a message in the textbox and click the "SEND" button. The chatbot will generate a response based on the input and previous messages in the conversation. You can continue the conversation by sending more messages.

## Project Structure

- `main.py`: Contains the code to launch the chatbot using Gradio.
- `openai_prompting.py`: Contains the `get_response` function that generates responses from the OpenAI API.
- `.env`: File containing the OpenAI API key as an environment variable.
