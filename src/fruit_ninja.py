import pygame
import sys


def run_game():
    # Initializing all imported pygame modules
    pygame.init()

    # Setup the screen: (screen width, screen height)
    screen = pygame.display.set_mode((1344, 756))

    # Set Caption
    pygame.display.set_caption('Fruit Ninja')

    # Background image for the game
    bg = pygame.image.load('images/bg.jpg')
    bg = pygame.transform.scale(bg, (1344, 756))

    # Starting the main loop for the game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Draw the background image on the Pygame surface
        screen.blit(bg, (0, 0))
        pygame.display.flip()

    # Create the screen


if __name__ == '__main__':
    run_game()