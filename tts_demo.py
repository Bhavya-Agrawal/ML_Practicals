#!/usr/bin/python3
from gtts import gTTS
import os
tts = gTTS(text="hello",lang="en")
# to save audio file in hello.mp3 at the same location as that of this file
tts.save("hello.mp3")
# starting the audio file using mpg321 driver
os.system("mpg321 hello.mp3")
