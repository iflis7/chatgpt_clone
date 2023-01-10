import gradio as gr
from gpt import get_response, PROMPT


def cloning_gpt(input, history):
    '''
        Function that generates a response based on a given input and conversation history.
        
        Parameters:
        - input (str): The input to generate a response for.
        - history (list): A list of tuples containing previous inputs and outputs in the conversation.
        
        Returns:
        - history (list): The updated conversation history with the new input and output appended.
        - history (list): A copy of the updated conversation history.
    '''
    history = history or []  # if history is None, set it to an empty list
    past = list(sum(history, ()))  # flatten the history list
    past.append(input)  # add the current input to the history
    inputs = ' '.join(past)  # join the history into a string
    output = get_response(inputs)  # get the model's response
    history.append(
        (input, output))  # add the current input and output to the history
    return history, history  # return the history as both the output and the state


block = gr.Blocks()

with block:
    gr.Markdown("""<h1><center>ChatGpt Clone "Bart version" </center></h1>""")
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder=PROMPT)
    state = gr.State()
    submit = gr.Button("SEND")
    submit.click(cloning_gpt,
                 inputs=[message, state],
                 outputs=[chatbot, state])

block.launch(
    debug=True, share=True
)  # debug=True to run locally and share=True to share the app publicaly
