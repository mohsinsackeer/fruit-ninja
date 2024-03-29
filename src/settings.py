import pygame

class Settings():

    def __init__(self) -> None:

        # Screen Settings
        self.screen_height = 900 #756
        self.screen_width = 900 #756  #1344
        self.screen_caption = 'Fruit Ninja'
        self.screen_img_loc = '../images/bg.jpg'

        # Music Settings
        self.bg_music_location = '../sounds/Fruit-Ninja-Theme-Song.mp3'
        self.fruit_slice_sound_location = '../sounds/Sword-swipe-1.wav'
        self.bomb_collision_sound_location = '../sounds/Bomb-explode.wav'
        self.fruit_slice_sound = pygame.mixer.Sound(self.fruit_slice_sound_location)
        self.bomb_collision_sound = pygame.mixer.Sound(self.bomb_collision_sound_location)

        # User (Timed) Event
        self.flying_object_timer_event = pygame.USEREVENT

        # Game Life Settings
        self.total_lives = 5

        # Button Text
        self.button_text = 'Play'

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
        
        pygame.time.set_timer(self.flying_object_timer_event,
                              self.flying_object_time_delay)

        # Scoring Points
        self.points_increment = 10
    
    def increase_speed(self):
        self.flying_object_speed += 0.1
    
    def reduce_time_delay(self):
        """
        This function create a new timed user event, to create new
        flying fruit/bomb. We have set 500 ms as the minimum time possible
        between the generation of two flying objects.
        """
        if self.flying_object_time_delay - 50 >= 500:
            self.flying_object_time_delay -= 50
        pygame.time.set_timer(self.flying_object_timer_event, 
                                self.flying_object_time_delay)
