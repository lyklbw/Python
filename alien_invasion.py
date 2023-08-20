

import pygame
from pygame.sprite import Group
from setting import Setting
from ship import Ship
from alien import Alien
import game_functions as gf     

def run_game():
    
    # Initialize game and create a screen object.
    pygame.init()
    #引入Setting类便于管理参数
    ai_setting = Setting()
    # Set the background color white.
    bg_color = (ai_setting.bg_color)
    #创建一个名为screen的显示窗口，实参（1200，800）是一个元组，指定游戏窗口尺寸
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    
    #引入Ship类,关于ship操作都在其中
    ship=Ship(ai_setting,screen)
    #use Group to store bullets and lyy
    bullets = Group()
    aliens=Group()
    #对游戏界面进行简单设置
    pygame.display.set_caption("Ikun Invasion")
    pygame.display.set_icon(pygame.image.load('images/ship.bmp'))

    gf.creat_fleet(ai_setting,screen,ship,aliens)
    
    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(ai_setting,screen,ship,bullets)
        #通过标志判断是否移动并执行
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(ai_setting,aliens)
        # Redraw the screen during each pass through the loop.        
        gf.update_screen(ai_setting, screen, ship,aliens,bullets)

run_game()  