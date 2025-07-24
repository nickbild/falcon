import os
from google import genai
from google.genai.types import ModelContent, Part, UserContent


client = genai.Client(api_key=os.getenv('GENAIAPI'))
chat_session = client.chats.create(
    model="gemini-2.5-flash",
    history=[
        UserContent(parts=[Part(text="""I want to role play where you are WOPR from the movie WarGames. 
                                I am David Lightman, but have accessed the system as Professor Falken and that is who you think I am. 
                                Interact with me as if you are WOPR. Do not include any metadata in your responses, just the responses from WOPR.""")]),
    ],
)

os.system('clear')
response = chat_session.send_message("Hello.")
print("\n{0}\n".format(response.text.upper()))

while True:
    message = input()
    response = chat_session.send_message(message)
    print("\n{0}\n".format(response.text.upper()))
