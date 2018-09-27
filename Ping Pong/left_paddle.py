"""
Name: Alexis Steven Garcia
Project: Ping Pong
Date: September 28, 2018
Email: AlexisSG96@csu.fullerton.edu
"""
import pygame
from pygame.sprite import Sprite


class LeftPaddle(Sprite):
    def __init__(self, ai_settings, screen):
        """Create the left_paddle and set its starting position."""
        super(LeftPaddle, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.rect = pygame.Rect(0, 0, ai_settings.left_paddle_width, ai_settings.left_paddle_height)
        self.screen_rect = screen.get_rect()
        self.color = ai_settings.left_paddle_color
        self.height = float(ai_settings.left_paddle_height)
        # Starts at the left of screen
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left + (self.screen_rect.right/16)
        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centery)
        # Movement flag for continuous movement
        self.moving_up = False
        self.moving_down = False

    def update(self, ai_settings):
        """Update the ship's position based on the movement flag."""
        if self.moving_up and self.rect.top > 0:
            self.center -= self.ai_settings.left_paddle_speed_factor
        if self.moving_down and self.rect.bottom < ai_settings.screen_width:
            self.center += self.ai_settings.left_paddle_speed_factor
        self.rect.centery = self.center

    def center_left_paddle(self):
        """Center the paddle on the screen."""
        self.center = self.screen_rect.midleft

    def draw_left_paddle(self):
        """Draw the paddle to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
