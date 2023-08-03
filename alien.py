import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Клас, що представляє одного прибульця з флоту"""
    def __init__(self, ai_game):
        """
        Purpose: 
        """
        super().__init__()
        self.screen = ai_game.screen
    # end def __init__
    pass

