import glob
import random
import pyttsx3
import keyboard

from audio import Audio
from mistral import Mistral


def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def main():
    audio = Audio(silent_frames=2)
    audio.set_while_silent(None)

    # ghosts = glob.glob("ghosts/*.txt")
    ghost = "ghosts/1.txt"

    mistral = Mistral(ghost)

    try:
        question = audio.get_transcript()
        print("Question:", question)
        answer = mistral(question)
        print("Answer:", answer)

        if keyboard.is_pressed('a'):  # if 'a' key is pressed
            text_to_speech(answer)  # it will convert the answer to audio and play it

    except KeyboardInterrupt:
        # break
        print("Bye!")


if __name__ == '__main__':
    main()
