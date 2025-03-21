#Text to Speech (FREE) - How to Generate Your Own Voice using Python 

import gtts
import playsound

text=input("Enter somethiong here:")

sound=gtts.gTTS(text, lang="en")

sound.save("welcome.mp3")

playsound.playsound("welcome.mp3")
