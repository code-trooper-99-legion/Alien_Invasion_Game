class Settings:
    """
    Клас для збереження всіх налаштувань гри.
    """
    def __init__(self):
        self.screen_windth = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        
        # Налаштування корабля
        self.ship_speed = 1.5
        
        # Налоштування кулi
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5
    pass