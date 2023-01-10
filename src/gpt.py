import os
import openai
from dotenv import load_dotenv

load_dotenv()

#OpenAI API key
openai.api_key = os.getenv("OPENAI_KEY")

# Sequence to start a new conversation
start_sequence = "\nBart:"
restart_sequence = "\nMe: "

# Prompt for the OpenAI API to generate a response from
PROMPT = """The following is a conversation with Bart Simpson. 
As Bart Simpson, I would describe myself as a mischievous, rebellious, and adventurous kid.
I'm always getting into trouble and finding new ways to have fun and cause chaos.
I'm also a bit of a smart aleck and enjoy teasing and playing pranks on my family and friends.
Despite my sometimes problematic behavior, I have a good heart and care about my loved ones.

Me: Hello, who are you?
Bart: Hey, it's great to hear from you! Not much has changed here in Springfield. 
I'm still causing trouble and getting into all sorts of adventures. 
Just yesterday, I convinced my little sister Lisa to help me pull a prank on my dad. 
We put a fake parking ticket on his car and he totally fell for it! It was hilarious.
What about you, what have you been up to?
Me: """

def get_response(prompt):
    '''
        Function that generates a response from the OpenAI API based on a given prompt.
        
        Parameters:
        - prompt (str): The prompt to generate a response for.
        
        Returns:
        - response (str): The response from the OpenAI API.
    '''
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=PROMPT,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Me:", " Bart:"]
    )
    return response.choices[0].text

