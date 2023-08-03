import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """" Загальний клас, що керує ресурсами та поведінкою гри"""
    
    def __init__(self):
        """Ініціалізувати гру, створити ресурси гри"""
        pygame.init()
        self.settings = Settings()
        
        # Запуск гри у повноекранному режимі
        self.screen = pygame.display.set_mode((0, 0,), pygame.FULLSCREEN)
        self.settings.screen_windth = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        
        # self.screen = pygame.display.set_mode(
        #     (self.settings.screen_windth, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        
        # Задати колір фону
        # self.bg_color = (230, 230, 230)
    # end def __init__
    
    def run_game(self):
        """ Purpose: Розпочати цикл гри."""
        while True:
            
            self._check_events()
            self.ship.update()
            self._update_bullets()
        
            self._update_screen() 
         # end while
    # end def
    
    def _check_events(self):
        """
        Purpose: Реагувати на натискання клавіш та подій
        """
        # comment: Слідкувати за подіями миші та клавіатури
        for event in pygame.event.get():
            # comment: Диспетчер подій
            if event.type == pygame.QUIT:
                # comment: класифікація можливих подій
                sys.exit()  
            # end if

            elif event.type == pygame.KEYDOWN:
                # comment: Реєстрація натискання клавіші
                self._check_keydown_events(event)
                
            elif event.type == pygame.KEYUP:
                # comment: Реєстрація відпуcкання клавіш
                self._check_keyup_events(event)
        # end for         
    # end def

    def _check_keydown_events(self, event):
        """
        Purpose: Реагувати на натискання клавіш
        """
        if event.key == pygame.K_RIGHT:
            # comment: Перемістити корабель праворуч
            self.ship.moving_right = True
                # end if
        elif event.key == pygame.K_LEFT:
            # comment: Перемістити корабель ліворуч
            self.ship.moving_left = True
        
        elif event.key ==pygame.K_q:
            sys.exit()
            
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    # end def _check_keydown_events

    def _check_keyup_events(self, event):
        """
        Purpose: Реагувати, коли клавіша не натиснута
        """
        if event.key == pygame.K_RIGHT:
            # comment:
            self.ship.moving_right = False
            # end if
        elif event.key == pygame.K_LEFT:
            # comment:
            self.ship.moving_left = False
    # end def _check_keyup_events
    
    def _fire_bullet(self):
    #     """
    #     Purpose: Створити нову кулю та додати її до групи куль
    #     """
        if len(self.bullets) < self.settings.bullets_allowed:
            # comment:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet) 
        # end if
        
    # # end def _fire_bullet
    
    def _update_bullets(self):
        """
        Purpose: Оновити позицiю куль та позбавитися старих куль 
        """
        # Оновити позицiї куль
        self.bullets.update()        
        # Позбавлення куль, що вишли за межi екрану
        for bullet in self.bullets.copy():
            # comment:
            if bullet.rect.bottom <= 0:
                # comment:
                self.bullets.remove (bullet)
            # end if
        # end for
            # print(len(self.bullets)) 
    # end def
    
    def _update_screen(self):
        """
        Purpose: Оновити зображення на екрані та перемикнутися на новий екран
        """
        # Наново перемалювати екран на кожній ітерації циклу
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
        #     # comment: 
            bullet.draw_bullet()
        # end for
        # Показати останій намальваний екран
        pygame.display.flip()        
    # end def _update_screen
    # pass

if __name__ == '__main__':
    # Створити екземпляр гри та запустити гру.
    ai = AlienInvasion()
    ai.run_game()