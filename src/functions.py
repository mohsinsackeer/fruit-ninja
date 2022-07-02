import sys
import pygame
import random
from settings import Settings
from flying_object import FlyingObject


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


def check_events(fn_settings, screen, flying_objects):

    """
    This function keeps tracks of the each event occuring
    during the game, and takes appropriate action.
    """

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == fn_settings.timer_event:
            obj = get_next_object(fn_settings, screen)
            flying_objects.add(obj)


def get_next_object(fn_settings, screen):
    # Fruit with a probability of 6/7
    # Bomb with a probability of 1/7
    fruit = random.randint(0, 6)
    if fruit:
        return FlyingObject(fn_settings, screen, bomb=False)
    else:
        return FlyingObject(fn_settings, screen, bomb=True)


def update_flying_objects(fn_settings, screen, flying_objects):
    flying_objects.update()

    # Get rid of objects that have disappeared
    for obj in flying_objects.copy():
        if (obj.rect.x<=0 or obj.rect.x>=fn_settings.screen_width) or\
            (obj.rect.y<=0 or obj.rect.y>=fn_settings.screen_height):
            flying_objects.remove(obj)
    print(len(flying_objects))
