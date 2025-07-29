# Falcon

Falcon simulates interacting with WOPR from the 1983 movie *WarGames* by using a Raspberry Pi 400, a vintage General Instrument SP0256-AL2 speech chip, and the Google Gemini LLM. The cool-retro-term terminal emulator completes the effect.

Shall we play a game?

![](https://raw.githubusercontent.com/nickbild/falcon/refs/heads/main/media/screenshot.jpg)

Now that is how we are really meant to talk to artificially superintelligent machines!

## How It Works

This [Python script](https://github.com/nickbild/falcon/blob/main/falcon.py) instructs a Google Gemini 2.5 Flash LLM to role play as if it were WOPR from the movie *WarGames*. As the user types (and as LLM responses come in), a sound is played mimicking the keypress sounds from the movie. Responses are also spoken in an appropriately robotic-sounding voice through an SP0256-AL2 speech chip from 1981 using my [GI-Pi Python library](https://github.com/nickbild/gi-pi). The lexconvert utility converts text strings into a list of allophone codes compatible with the chip. The cool-retro-term terminal emulator, with a custom profile, simulates interacting with WOPR on a 1980s CRT computer monitor resembling the one in the movie. 

## Media

![](https://raw.githubusercontent.com/nickbild/falcon/refs/heads/main/media/hardware_sm.jpg)

![](https://raw.githubusercontent.com/nickbild/falcon/refs/heads/main/media/running_falcon_sm.jpg)

## Bill of Materials

- 1 x Raspberry Pi 400
- 1 x SP0256-AL2 speech chip and audio amplification circuit (see [GI-Pi](https://github.com/nickbild/gi-pi))
- 1 x USB speaker
- 1 x TRRS speaker

## About the Author

[Nick A. Bild, MS](https://nickbild79.firebaseapp.com/#!/)
