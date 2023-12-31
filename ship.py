import pygame
import setting
class Ship():
    """A class to manage the ship."""
    def __init__(self,ai_setting,screen):
        self.screen = screen
        self.ai_setting = ai_setting
        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_setting.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.ai_setting.ship_speed_factor
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

