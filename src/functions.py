import sys
import pygame
import random
from game_stats import GameStats
from settings import Settings
from flying_object import FlyingObject


def initialize_game_components():

    """
    This function initializes:
    -> Pygame Modules
    -> Fruit Ninja Settings
    -> Screen
    -> Timer for introducing flying objects
    """

    pygame.init()
    fn_settings = Settings()
    screen = pygame.display.set_mode((fn_settings.screen_width, fn_settings.screen_height))
    pygame.display.set_caption(fn_settings.screen_caption)
    background_image = pygame.image.load(fn_settings.screen_img_loc)
    background_image = pygame.transform.scale(background_image, (fn_settings.screen_width, fn_settings.screen_height))
    stats = GameStats(fn_settings)
    stats.reset_stats()
    pygame.time.set_timer(fn_settings.flying_object_timer_event, fn_settings.flying_object_time_delay)
    return fn_settings, screen, background_image, stats


def check_events(fn_settings, screen, flying_objects):

    """
    This function keeps tracks of the each event occuring
    during the game, and takes appropriate action.
    """

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == fn_settings.flying_object_timer_event:
            obj = get_next_object(fn_settings, screen)
            flying_objects.add(obj)
    
    check_object_mouse_collision(flying_objects)


def get_next_object(fn_settings, screen):
    # Fruit with a probability of 6/7
    # Bomb with a probability of 1/7
    fruit = random.randint(0, 6)
    if fruit:
        return FlyingObject(fn_settings, screen, bomb=False)
    else:
        return FlyingObject(fn_settings, screen, bomb=True)


def check_object_mouse_collision(flying_objects):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for obj in flying_objects.copy():
        collided = obj.rect.collidepoint(mouse_x, mouse_y)
        if collided:
            if obj.fruit:
                flying_objects.remove(obj)
            else:
                sys.exit()


def update_flying_objects(fn_settings, stats, flying_objects):
    flying_objects.update()

    # Get rid of objects that have disappeared
    for obj in flying_objects.copy():
        if (obj.rect.x<=0 or obj.rect.x>=fn_settings.screen_width) or\
            (obj.rect.y<=0 or obj.rect.y>=fn_settings.screen_height):
            flying_objects.remove(obj)
            if obj.fruit:
                stats.lives_left -= 1
                if not stats.lives_left:
                    sys.exit()            
