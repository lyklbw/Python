import sys# sys module allows us to exit the game when the player quits
import pygame
from bullet import Bullet
from alien import Alien

def fire_bullet(ai_setting,screen,ship,bullets):
    """Fire a bullet if limit not reached yet."""
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < ai_setting.bullet_allowed:
        new_bullet = Bullet(ai_setting, screen, ship)
        #加入group中
        bullets.add(new_bullet)

def check_keydown_events(event, ai_setting,screen,ship,bullets):
    """Respond to keypresses."""    
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True             
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_setting,screen,ship,bullets)
    elif event.key == pygame.K_q:#大写Q
        sys.exit()



def check_keyup_events(event, ship):
    """Respond to key releases."""    
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False             
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_setting,screen,ship,bullets):
    """Respond to keypresses and mouse events."""
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #按键按下
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_setting,screen,ship,bullets)
        #按键松开
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
       

def update_screen(ai_setting, screen, ship,aliens,bullets):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.        
    screen.fill(ai_setting.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)
    # Make the most recently drawn screen visible.
    pygame.display.flip()

def update_bullets(bullets):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions.
    bullets.update()
    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
def get_number_aliens_x(ai_setting, alien_width):
        available_space_x = ai_setting.screen_width
        number_aliems_x = int(available_space_x / (2 * alien_width))
        return number_aliems_x

    
def creat_alien(ai_setting,screen,aliens,alien_number,row_number):
        alien=Alien(ai_setting,screen)
        alien_width=alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x=alien.x
        alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
        aliens.add(alien)


def get_number_rows(ai_setting,ship_height,alien_height):
        availabe_space_y=(ai_setting.screen_height-(3 * alien_height)-ship_height)
        number_rows=int(availabe_space_y/(2*alien_height))
        return number_rows

def creat_fleet(ai_setting,screen,ship,aliens):
        alien=Alien(ai_setting,screen)
        number_aliens_x=get_number_aliens_x(ai_setting,alien.rect.width)
        number_rows=get_number_rows(ai_setting,ship.rect.height,alien.rect.height)
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                creat_alien(ai_setting,screen,aliens,alien_number,row_number)

def check_fleet_edges(ai_setting,aliens):
        for alien in aliens.sprites():
            if alien.check_edge():
                change_fleet_direction(ai_setting,aliens)
                break
def change_fleet_direction(ai_setting,aliens):
        for alien in aliens.sprites():
            alien.rect.y += ai_setting.fleet_drop_speed
        ai_setting.fleet_direction *= -1


def update_aliens(ai_setting,aliens):
        check_fleet_edges(ai_setting,aliens)
        aliens.update()



