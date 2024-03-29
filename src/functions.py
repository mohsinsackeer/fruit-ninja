import sys
import pygame
import random
from game_stats import GameStats
from settings import Settings
from flying_object import FlyingObject
from scoreboard import ScoreBoard
from button import Button


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
    pygame.mixer.music.load(fn_settings.bg_music_location)
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)
    stats = GameStats(fn_settings)
    sb = ScoreBoard(screen, stats)
    button = Button(fn_settings, screen)
    return fn_settings, screen, background_image, stats, sb, button


def check_events(fn_settings, screen, stats, flying_objects, button):

    """
    This function keeps tracks of the each event occuring
    during the game, and takes appropriate action.
    """

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == fn_settings.flying_object_timer_event:
            if stats.game_active:
                release_next_object(fn_settings, screen, stats, flying_objects)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            check_button_clicked(fn_settings, stats, button)

    check_object_mouse_collision(fn_settings, stats, flying_objects)


def release_next_object(fn_settings, screen, stats, flying_objects):
    stats.event_counter += 1
    if stats.event_counter % 10 == 0:
        stats.level_up()
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


def check_object_mouse_collision(fn_settings, stats, flying_objects):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for obj in flying_objects.copy():
        collided = obj.rect.collidepoint(mouse_x, mouse_y)
        if collided:
            if obj.fruit:
                fn_settings.fruit_slice_sound.play()
                flying_objects.remove(obj)
                stats.award_points()
            else:
                fn_settings.bomb_collision_sound.play()
                game_ends(stats, flying_objects)

def check_button_clicked(fn_settings, stats, button):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    button_clicked = button.rect.collidepoint(mouse_x, mouse_y)

    if button_clicked and not stats.game_active:
        fn_settings.reset_settings()
        stats.reset_stats()
        stats.game_active = True


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
                    game_ends(stats, flying_objects)

def game_ends(stats, flying_objects):
    stats.game_active = False
    flying_objects.empty()    
