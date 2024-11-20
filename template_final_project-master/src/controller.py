import pygame
from player import Player
from enemy import Enemy

def __init__(self):
    """
    docstring
    """
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
        pygame.display.flip()
