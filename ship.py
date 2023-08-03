import pygame


class Ship:
    """
    Клас для керування кораблем
    """
    def __init__(self, ai_game):
        """
        Purpose: Ініціалізувати корабель та задати його початкову позицію
        """
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        # Завантажити зображнння корабля та отримати його в rect
        self.image = pygame.image.load('images/my_ship.bmp')
        self.rect = self.image.get_rect()
        
        # Створювати кожен новий корабель внизу екрана, по центру
        self.rect.midbottom = self.screen_rect.midbottom
        
        # Зберегти десяткове значення для позиції корабля по горизонталі
        self.x = float(self.rect.x)

        # Індикатор руху
        self.moving_right = False
        self.moving_left = False
    # end def __init__
        
    def update(self):
        """
        Purpose: Оновити поточну позицію корабля на основі індикатору руху
        """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # comment: Оновити значення ship.x, а не rect.
            self.x += self.settings.ship_speed
        # end if
        if self.moving_left and self.rect.left > 0 :
            # comment:
            self.x -= self.settings.ship_speed
        # end if
        
        # Оновити об'єкт rect з self.x
        self.rect.x = self.x
        
    # end def update
        
    def blitme (self):
        """
        Purpose: Намалювати корабель у його поточному розташуванні 
        """
        self.screen.blit(self.image, self.rect)
    
    # end def blitme
    pass