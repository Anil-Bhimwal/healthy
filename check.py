import pygame
import datetime
import math as mth
pygame.init()
pygame.display.set_mode((1000,100))
pygame.mixer.music.load('physical.mp3')
pygame.mixer.music.play(0)
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)