class GameStats():

    def __init__(self, fn_settings) -> None:
        self.fn_settings = fn_settings
        self.reset_stats()
    
    def reset_stats(self):
        self.lives_left = self.fn_settings.total_lives
        self.score = 0
        self.level = 1