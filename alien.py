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
        
        # Додавання зображення прибульця й налаштування атрибуту rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        # Початок кожного нового прибульця у верхньому лівому куті екрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # збереження інопланетян в точному горизонтальному положенні
        self.x = float(self.rect.x)
    # end def __init__
    # pass

