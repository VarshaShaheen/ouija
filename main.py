import glob
import random

from audio import Audio
from mistral import Mistral


def main():
    audio = Audio(silent_frames=2)
    audio.set_while_silent(None)

    ghosts = glob.glob("ghosts/1.txt")
    ghost = random.choice(ghosts)

    mistral = Mistral(ghost)

    try:
        question = audio.get_transcript()
        print("Question:", question)
        answer = mistral(question)
        print("Answer:", answer)

    except KeyboardInterrupt:
        # break
        print("Bye!")


if __name__ == '__main__':
    main()
