"""
Name: Alexis Steven Garcia
Project: Ping Pong
Date: September 28, 2018
Email: AlexisSG96@csu.fullerton.edu
"""


class Settings:
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        self.test = (100, 100, 100)

        # left paddle settings
        self.left_paddle_width = self.screen_width/30
        self.left_paddle_height = self.screen_height/4
        self.left_paddle_color = 255, 255, 255
        self.left_paddle_speed_factor = 1.5
        self.left_paddle_limit = 1

        # right paddle settings
        self.right_paddle_width = self.screen_width/30
        self.right_paddle_height = self.screen_height/4
        self.right_paddle_color = 255, 255, 255
        self.right_paddle_speed_factor = 1.5
        self.right_paddle_limit = 1
        self.right_paddle_y_direction = 1

        # ball settings
        self.ball_speed_factor = 1
        self.ball_width = 15
        self.ball_height = 15
        self.ball_color = 255, 255, 255
        self.balls_allowed = 1
        self.ball_x_direction = 1
        self.ball_y_direction = 1

        # pong scoring
        self.level = 1
        self.points = 1
        self.player_score = 1
        self.cpu_score = 1
