import pygame
from pygame.sprite import Sprite#Sprite类可以将游戏中相关的元素编组，进而同时操作编组中的所有元素


class Alien(Sprite):
    def __init__(self,ai_setting,screen):
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_setting = ai_setting
        
        #load the alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        #start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #store the alien's exact position
        self.x = float(self.rect.x)
        
    def blitme(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image,self.rect)
    
        
    def check_edge(self):
        """Return True if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <=0:
            return True
    
    def update(self):
        """Move the alien right"""
        self.x +=( self.ai_setting.alien_speed_factor*self.ai_setting.fleet_direction )
        self.rect.x = self.x


    
        
        