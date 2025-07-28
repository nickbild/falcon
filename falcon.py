import os
from google import genai
from google.genai.types import ModelContent, Part, UserContent
import sys
import time
import threading
import random
from evdev import InputDevice, categorize, ecodes
import glob
from playsound import playsound


whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ')


def find_keyboard_device_paths():
    """
    Attempts to find all devices that appear to be keyboards.
    Returns a list of device paths (e.g., '/dev/input/eventX').
    """
    device_paths = glob.glob('/dev/input/event*')
    keyboard_paths = []
    
    print("Scanning for input devices...", file=sys.stderr)
    for path in device_paths:
        dev = InputDevice(path)
        if ecodes.EV_KEY in dev.capabilities() and \
            (ecodes.KEY_Q in dev.capabilities()[ecodes.EV_KEY] or \
            ecodes.KEY_A in dev.capabilities()[ecodes.EV_KEY] or \
            ecodes.KEY_1 in dev.capabilities()[ecodes.EV_KEY]):
                
            print(f"  Found potential keyboard: {dev.path} ({dev.name})", file=sys.stderr)
            keyboard_paths.append(path)
        dev.close() # Close device after checking capabilities

    return keyboard_paths


def read_device_events(device_path):
    dev = InputDevice(device_path)
    print(f"Successfully monitoring: {dev.path} ({dev.name})")
        
    for event in dev.read_loop():
        if event.type == ecodes.EV_KEY:
            if event.value == 1: # Key down. 
                playsound("typing_sound.wav")


client = genai.Client(api_key=os.getenv('GENAIAPI'))
chat_session = client.chats.create(
    model="gemini-2.5-flash",
    history=[
        UserContent(parts=[Part(text="""I want to role play where you are WOPR from the movie WarGames. 
                                I am David Lightman, but have accessed the system as Professor Falken and that is who you think I am. 
                                Interact with me as if you are WOPR. Do not include any metadata in your responses, just the responses from WOPR.""")]),
    ],
)


keyboard_device_paths = find_keyboard_device_paths()

active_threads = []
for path in keyboard_device_paths:
    thread = threading.Thread(target=read_device_events, args=(path,))
    thread.daemon = True # Allow main program to exit even if threads are running
    active_threads.append(thread)
    thread.start()

os.system('clear')
response = chat_session.send_message("Hello.")
print("\n{0}\n".format(response.text.upper()))

say_it = ''.join(filter(whitelist.__contains__, response.text.upper()))
os.system("python3 speech.py '{0}'".format(say_it))

while True:
    message = input()
    response = chat_session.send_message(message)
    print("\n{0}\n".format(response.text.upper()))

    say_it = ''.join(filter(whitelist.__contains__, response.text.upper()))
    os.system("python3 speech.py '{0}'".format(say_it))

