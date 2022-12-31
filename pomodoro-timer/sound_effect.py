import pygame

sound = pygame.mixer

pygame.init()

WORK = sound.Sound(file='sounds/work.mp3')

RELAX = sound.Sound(file='sounds/relax.mp3')
RELAX.set_volume(0.3)
