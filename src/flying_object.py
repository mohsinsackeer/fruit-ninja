import pygame
from pygame.sprite import Sprite
import random


class FlyingObject(Sprite):
    
    def __init__(self, fn_settings, screen, bomb=False) -> None:
        super().__init__()

        self.fn_settings = fn_settings
        self.screen = screen

        if bomb:
            self.image = pygame.image.load(fn_settings.bomb_location)
        else:
            index = random.randint(0, len(fn_settings.fruit_locations.values())-1)
            self.image = pygame.image.load(list(fn_settings.fruit_locations.values())[index])
        
        self.rect = self.image.get_rect()

        self.start_loc_id = random.randint(1, 8)
        self.rect.x = self.fn_settings.popup_locations[1]['x']
        self.rect.y = self.fn_settings.popup_locations[1]['y']

        if self.start_loc_id in [3,4,7,8]:
            self.y_dir = 0
            # self.loc = float(self.rect.x)
            if self.start_loc_id in [7,8]:
                self.x_dir = 1
            else:
                self.x_dir = -1
        else:
            self.x_dir = 0
            # self.loc = float(self.rect.y)
            if self.start_loc_id in [1,2]:
                self.y_dir = 1
            else:
                self.y_dir = -1
    
    def update(self) -> None:
        self.loc += (self.x_dir + self.y_dir) * 1
        if self.x_dir:
            self.rect.x = self.loc
        else:
            self.rect.y = self.loc
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)
    