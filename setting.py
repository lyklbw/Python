class Setting():
    
    def __init__(self):
        #initialize the game's settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)
        self.ship_speed_factor = 1
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0,0,0)
        self.bullet_allowed = 3
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 10
        #fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1