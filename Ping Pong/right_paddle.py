"""
Name: Alexis Steven Garcia
Project: Ping Pong
Date: September 28, 2018
Email: AlexisSG96@csu.fullerton.edu
"""
import pygame
from pygame.sprite import Sprite


class RightPaddle(Sprite):
    def __init__(self, ai_settings, screen):
        """Create the Right_Paddle and set its starting position."""
        super(RightPaddle, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.rect = pygame.Rect(0, 0, ai_settings.right_paddle_width, ai_settings.right_paddle_height)
        self.screen_rect = screen.get_rect()
        self.color = ai_settings.right_paddle_color
        self.height = float(ai_settings.right_paddle_height)
        # Paddle starts at the right
        self.rect.centery = self.screen_rect.centery
        self.rect.right = self.screen_rect.right - (self.screen_rect.right/16)
        # Store a decimal value for the ship's center.
        self.y = float(self.rect.y)
        # Movement flag for continuous movement
        self.moving_up = False
        self.moving_down = False
        self.center = None

    def update(self, ai_settings):
        """Update the paddles position based on the movement flag."""
        self.y += (ai_settings.right_paddle_y_direction * ai_settings.right_paddle_speed_factor)
        self.rect.y = self.y
        if self.moving_up and self.rect.top > 0:
            self.center -= self.ai_settings.right_paddle_speed_factor
        if self.moving_down and self.rect.bottom < ai_settings.screen_height:
            self.center += self.ai_settings.right_paddle_speed_factor

    def check_edges(self):
        """Check if paddle hits an edge"""
        if self.rect.top <= 0:
            return True
        elif self.rect.bottom >= 800:
            return True

    def center_right_paddle(self):
        """Center the paddle on the screen."""
        self.center = self.screen_rect.midright

    def draw_right_paddle(self):
        """Draw the paddle to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
