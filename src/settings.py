import pygame

class Settings():

    def __init__(self) -> None:

        # Screen Settings
        self.screen_height = 756
        self.screen_width = 756  #1344
        self.screen_caption = 'Fruit Ninja'
        self.screen_img_loc = '../images/bg.jpg'

        # Flying Object Settings
        self.flying_object_time_delay = 1000
        self.flying_object_timer_event = pygame.USEREVENT
        self.flying_object_speed = 1
        
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
