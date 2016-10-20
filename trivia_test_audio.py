# import pyttsx
# 
# engine = pyttsx.init()
# engine.say("Hello! My name is Lisa. I'll be your host of this game. You will get one dollar for each question answered correctlly. Are you ready? Let's start the game!")
# #engine.say('Pay more attention. OK?')
# engine.runAndWait()


import pygame

import time

pygame.init()

pygame.mixer.music.load("test.wav")

pygame.mixer.music.play()

time.sleep(10)