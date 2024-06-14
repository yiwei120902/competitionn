import chainlit as cl
from chat import get_response

@cl.on_chat_start
async def start():
    await cl.Message(content="Hello! How can I assist you today?").send()

@cl.on_message
async def handle_message(message):
    response = get_response(message.content)
    await cl.Message(content=response).send()

if __name__ == "__main__":
    cl.run()
