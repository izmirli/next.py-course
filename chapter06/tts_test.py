"""Play text-to-speech"""
from gtts import gTTS
import os
from playsound import playsound

# import pyttsx
# from io import BytesIO
# import musicplayer
# import pygame

MP3_FILE_NAME = f"tts_{os.getpid()}.mp3"
tts = gTTS(text='first time i\'m using a package in next.py course.', lang='en')
tts.save(MP3_FILE_NAME)
playsound(MP3_FILE_NAME)

# pygame.mixer.init()
# pygame.mixer.music.load(MP3_FILE_NAME)
# pygame.mixer.music.play()
# pygame.quit()

# os.system("mpg321 good.mp3")

os.remove(MP3_FILE_NAME)

# mp3_fp = BytesIO()
# tts.write_to_fp(mp3_fp)

# ---
# engine = pyttsx.init()
# engine.say("first time i'm using a package in next.py course.")
# engine.runAndWait()
