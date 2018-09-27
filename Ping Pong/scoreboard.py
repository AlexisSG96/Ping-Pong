"""
Name: Alexis Steven Garcia
Project: Ping Pong
Date: September 28, 2018
Email: AlexisSG96@csu.fullerton.edu
"""
import pygame.font


class Scoreboard:
    """A class to report scoring information."""
    def __init__(self, ai_settings, screen, stats):
        """Initialize score keeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Font settings for scoring information.
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Score images
        self.player_score_image = None
        self.cpu_score_image = None
        self.player_score_rect = None
        self.cpu_score_rect = None
        self.high_score_image = None
        self.high_score_rect = None

        # Line separating paddles
        self.line_rect = pygame.Rect(0, 0, 2, ai_settings.screen_height)
        self.screen_rect = screen.get_rect()
        self.line_color = (255, 255, 255)
        self.height = float(ai_settings.screen_height)
        self.line_rect.centerx = self.screen_rect.centerx
        self.center = float(self.line_rect.centerx)

        # Prepare the initial score image.
        self.prep_player_score()
        self.prep_cpu_score()
        self.prep_high_score()
        self.prep_mid_line()

    def prep_player_score(self):
        rounded_score = self.stats.player_score
        player_score_str = str(rounded_score)
        self.player_score_image = self.font.render(player_score_str, True, self.text_color, self.ai_settings.bg_color)

        # Display the score at the top left of the screen
        self.player_score_rect = self.player_score_image.get_rect()
        self.player_score_rect.left = self.screen_rect.left + (self.screen_rect.right/4)
        self.player_score_rect.top = 20

    def prep_cpu_score(self):
        rounded_score = self.stats.cpu_score
        cpu_score_str = str(rounded_score)
        self.cpu_score_image = self.font.render(cpu_score_str, True, self.text_color, self.ai_settings.bg_color)

        # Display the score at the top right of the screen
        self.cpu_score_rect = self.cpu_score_image.get_rect()
        self.cpu_score_rect.right = self.screen_rect.right - (self.screen_rect.right/4)
        self.cpu_score_rect.top = 20

    def prep_high_score(self):
        high_score = self.stats.high_score
        high_score_str = str(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)

        # Center the high score at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.player_score_rect.top

    def prep_mid_line(self):
        pygame.draw.rect(self.screen, self.line_color, self.line_rect)

    def show_score(self):
        self.screen.blit(self.player_score_image, self.player_score_rect)
        self.screen.blit(self.cpu_score_image, self.cpu_score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
