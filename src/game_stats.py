class GameStats():

    def __init__(self, fn_settings) -> None:
        self.fn_settings = fn_settings
        self.game_active = False
        self.high_score = 0
        self.reset_stats()
    
    def reset_stats(self):
        self.lives_left = self.fn_settings.total_lives
        self.score = 0
        self.level = 1
        self.event_counter = 0
    
    def level_up(self):
        self.level += 1
        # Adjust Speed
        self.fn_settings.increase_speed()
        # Adjust Rate by changing the timer event
        self.fn_settings.reduce_time_delay()
    
    def award_points(self):
        self.score = self.score + self.fn_settings.points_increment
        if self.score > self.high_score:
            self.high_score = self.score
