import pygame
import functions as F
from pygame.sprite import Group


def run_game():

    """
    This function is responsible for running the entire
    Fruit Ninja game.
    """

    fn_settings, screen, background_image, stats, sb = F.initialize_game_components()
    flying_objects = Group()

    # Starting the main loop for the game
    while True:
        F.check_events(fn_settings, screen, stats, flying_objects)

        # Update the position of fruit
        F.update_flying_objects(fn_settings, stats, flying_objects)

        # Draw the background image on the Pygame surface
        screen.blit(background_image, (0, 0))
        flying_objects.draw(screen)
        sb.show_scoreboard()

        # Display the new screen
        pygame.display.flip()


if __name__ == '__main__':
    run_game()
    