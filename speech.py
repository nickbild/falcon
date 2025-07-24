from gi_sound import GiSpeech
import time
import subprocess
import sys


def main():
    speech = GiSpeech(a1=37, a2=35, a3=33, a4=31, a5=29, a6=23, ald=21, sby=15, rst=13)
    
    speak = sys.argv[1]

    # Convert text into allophones.
    output = subprocess.check_output("python3 -m lexconvert --phones cheetah '{0}'".format(speak), shell=True)
    result = output.decode('ascii').strip().replace("DATA ", "").split(",")

    # Speak the allphones.
    for allophone in result:
        speech.speak(int(allophone))

    return


if __name__ == "__main__":
    main()
