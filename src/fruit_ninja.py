import pygame
import functions as F
from flying_object import FlyingObject


def run_game():

    """
    This function is responsible for running the entire
    Fruit Ninja game.
    """

    fn_settings, screen, background_image = F.initialize_game_components()
    obj = FlyingObject(fn_settings, screen, bomb=True)

    # Starting the main loop for the game
    while True:
        F.check_events()

        # Draw the background image on the Pygame surface
        screen.blit(background_image, (0, 0))
        obj.blitme()

        # Display the new screen
        pygame.display.flip()


if __name__ == '__main__':
    run_game()