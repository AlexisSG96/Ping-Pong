"""
Name: Alexis Steven Garcia
Project: Ping Pong
Date: September 28, 2018
Email: AlexisSG96@csu.fullerton.edu
"""
import pygame
from pygame.sprite import Sprite


class Ball(Sprite):
    """A class to manage the ball."""
    def __init__(self, ai_settings, screen, left_paddle):
        """Create a ball object at middle."""
        super(Ball, self).__init__() 
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Create a ball object at the middle and then set correct position and size.
        self.rect = pygame.Rect(0, 0, ai_settings.ball_width, ai_settings.ball_height)
        self.rect.centery = self.screen_rect.centery 
        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.rect.top
        self.rect.bottom = self.rect.bottom

        # Store the ball's position as a decimal value. 
        self.x = float(self.rect.x) 
        self.y = float(self.rect.y) 
        self.color = ai_settings.ball_color 
        self.speed_factor = ai_settings.ball_speed_factor 

    def collision_left_right(self, left_paddle, right_paddle):
        """Check if ball collides with paddles."""
        if self.rect.colliderect(left_paddle.rect): 
            return True 
        if self.rect.colliderect(right_paddle.rect): 
            return True 

    def collision_top_bottom(self, top_paddle, bottom_paddle):
        """Check if ball collides with top and bottom of screen."""
        if self.rect.colliderect(top_paddle.rect): 
            return True 
        if self.rect.colliderect(bottom_paddle.rect): 
            return True 

    def check_edges_horizontal(self): 
        """Return True if ball is at edge of screen."""
        screen_rect = self.screen.get_rect() 
        if self.rect.right >= screen_rect.right: 
            return True 
        elif self.rect.left <= screen_rect.left:
            return True 

    def check_edges_vertical(self):
        """Return True if ball is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.top:
            return True 
        elif self.rect.top <= screen_rect.bottom:
            return True
 
    def update(self, ai_settings): 
        """Ball will move diagonally."""
        self.x += (ai_settings.ball_x_direction * ai_settings.ball_speed_factor)
        self.rect.x = self.x
        self.y -= (ai_settings.ball_y_direction * ai_settings.ball_speed_factor)
        self.rect.y = self.y
        
    def draw_ball(self): 
        """Draw the ball on the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect) 
