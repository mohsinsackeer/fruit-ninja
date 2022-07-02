import pygame

class Settings():

    def __init__(self) -> None:

        # Screen Settings
        self.screen_height = 756
        self.screen_width = 756  #1344
        self.screen_caption = 'Fruit Ninja'
        self.screen_img_loc = '../images/bg.jpg'

        # Game Life Settings
        self.total_lives = 5

        # Image Locations
        self.fruit_locations = {
            'coconut' : '../images/coconut.bmp',
            'pineapple' : '../images/pineapple.bmp',
            'pumpkin' : '../images/pumpkin.bmp',
            'tomato' : '../images/tomato.bmp',
            'watermelon' : '../images/watermelon.bmp'
        }
        self.bomb_location = '../images/bomb.bmp'

        # Object Pop Up Locations
        self.popup_locations = {
            1   :   {'x':self.screen_width*0.2, 'y':0},
            2   :   {'x':self.screen_width*0.8, 'y':0},
            3   :   {'x':self.screen_width, 'y':self.screen_height*0.2},
            4   :   {'x':self.screen_width, 'y':self.screen_height*0.8},
            5   :   {'x':self.screen_width*0.8, 'y':self.screen_height},
            6   :   {'x':self.screen_width*0.2, 'y':self.screen_height},
            7   :   {'x':0, 'y':self.screen_height*0.8},
            8   :   {'x':0, 'y':self.screen_height*0.2}
        }
        self.reset_settings()
    
    def reset_settings(self):
        # Flying Object Settings
        # Flying Object Settings changes with Level Up
        self.flying_object_speed = 1
        self.flying_object_time_delay = 1000
        self.flying_object_timer_event = pygame.USEREVENT + 1
    
    def increase_speed(self):
        self.flying_object_speed += 0.1
    
    def reduce_time_delay(self, level):
        """
        This function create a new timed user event, to create new
        flying fruit/bomb. We have set 500 ms as the minimum time possible
        between the generation of two flying objects.
        """
        if self.flying_object_time_delay - 50 >= 500:
            self.flying_object_time_delay -= 50
        self.flying_object_timer_event = pygame.USEREVENT + level
        pygame.time.set_timer(self.flying_object_timer_event, 
                                self.flying_object_time_delay)
