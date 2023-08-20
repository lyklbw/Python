import pygame
from pygame.sprite import Sprite#Sprite类可以将游戏中相关的元素编组，进而同时操作编组中的所有元素
from setting import Setting
class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""
    def __init__(self,ai_setting,screen,ship):
        super(Bullet,self).__init__()#super()是一个特殊函数，帮助python将父类和子类关联起来
        self.screen = screen

        #create a bullet rect at (0,0) and then set correct position
        self.rect = pygame.Rect(0,0,ai_setting.bullet_width,ai_setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top-10

        #store the bullet's position as a decimal value
        self.y = float(self.rect.y)

        self.color = ai_setting.bullet_color
        self.speed_factor = ai_setting.bullet_speed_factor
   
   
    def update(self):
        """Move the bullet up the screen"""
        #update the decimal position of the bullet
        self.y -= self.speed_factor
        #update the rect position
        self.rect.y = self.y
        
    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen,self.color,self.rect)
        
    

    

