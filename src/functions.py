import sys
import pygame
from settings import Settings


def initialize_game_components():

    """
    This function initializes:
    -> Pygame Modules
    -> Fruit Ninja Settings
    -> Screen
    """

    pygame.init()
    fn_settings = Settings()
    screen = pygame.display.set_mode((fn_settings.screen_width, fn_settings.screen_height))
    pygame.display.set_caption(fn_settings.screen_caption)
    background_image = pygame.image.load('../images/bg.jpg')
    background_image = pygame.transform.scale(background_image, (fn_settings.screen_width, fn_settings.screen_height))
    return fn_settings, screen, background_image


def check_events():

    """
    This function keeps tracks of the each event occuring
    during the game, and takes appropriate action.
    """

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


pass