import pygame

class ScoreBoard():

    def __init__(self, screen, stats) -> None:
        self.screen = screen
        self.stats = stats

        self.screen_rect = self.screen.get_rect()
        self.text_color = (230, 230, 230)
        self.font = pygame.font.SysFont(None, 48)
    
    def prep_level(self):
        level_str = f"Level: {self.stats.level}"
        self.level_image = self.font.render(level_str, True,
                                            self.text_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.centerx = self.screen_rect.centerx
        self.level_rect.bottom = self.score_rect.top - 5

    
    def prep_score(self):
        """
        Turns the score into a rendered image to be displayed.
        """
        score = int(self.stats.score)
        score_str = f"Score: {score}"
        self.score_image = self.font.render(score_str, True,
                                            self.text_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.centerx = self.screen_rect.centerx
        self.score_rect.bottom = self.lives_left_rect.top - 5
    
    def prep_lives_left(self):
        lives_left_str = f"Lives Left: {self.stats.lives_left}"
        self.lives_left_image = self.font.render(lives_left_str, True,
                                            self.text_color)
        self.lives_left_rect = self.lives_left_image.get_rect()
        self.lives_left_rect.centerx = self.screen_rect.centerx
        self.lives_left_rect.bottom = self.screen_rect.bottom - 5

    def show_score(self):
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.lives_left_image, self.lives_left_rect)

    def show_scoreboard(self):
        self.prep_lives_left()
        self.prep_score()
        self.prep_level()
        self.show_score()