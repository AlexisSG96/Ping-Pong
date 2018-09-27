"""
Name: Alexis Steven Garcia
Project: Ping Pong
Date: September 28, 2018
Email: AlexisSG96@csu.fullerton.edu
"""
import sys
import pygame
from ball import Ball


def check_play_button(ai_settings, screen, stats, sb, play_button, left_paddle, balls, mouse_x, mouse_y):
    """Check if play button is pressed."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)

        # Reset the game statistics
        stats.reset_stats()
        stats.game_active = True

        # Reset the scoreboard images
        sb.prep_player_score()
        sb.prep_cpu_score()
        sb.prep_high_score()
        balls.empty()


def check_events(ai_settings, screen, stats, sb, play_button, left_paddle, balls):
    """Check status of key presses."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, left_paddle, balls)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, left_paddle)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, left_paddle, balls, mouse_x, mouse_y)


def check_keydown_events(event, ai_settings, screen, left_paddle, balls):
    """Check if keys are pressed."""
    if event.key == pygame.K_UP:
        left_paddle.moving_up = True
    elif event.key == pygame.K_DOWN:
        left_paddle.moving_down = True
    elif event.key == pygame.K_w:
        left_paddle.moving_up = True
    elif event.key == pygame.K_s:
        left_paddle.moving_down = True
    elif event.key == pygame.K_SPACE:
        ball_start(ai_settings, screen, left_paddle, balls)


def ball_start(ai_settings, screen, left_paddle, balls):
    """Create a new ball."""
    if len(balls) < ai_settings.balls_allowed:
        new_ball = Ball(ai_settings, screen, left_paddle)
        balls.add(new_ball)


def check_keyup_events(event, left_paddle):
    """Check to see when keys are no longer pressed."""
    if event.key == pygame.K_UP:
        left_paddle.moving_up = False
    elif event.key == pygame.K_DOWN:
        left_paddle.moving_down = False
    elif event.key == pygame.K_w:
        left_paddle.moving_up = False
    elif event.key == pygame.K_s:
        left_paddle.moving_down = False


def check_high_scores(stats, sb):
    """Check to see if there's a new high score."""
    if stats.player_score > stats.high_score:
        stats.high_score = stats.player_score
    sb.prep_high_score()


def check_ball_edges(ai_settings, balls):
    """Used to change ball direction"""
    for ball in balls.sprites():
        if ball.check_edges_horizontal():
            change_ball_direction_horizontal(ai_settings, balls)
            break
        elif ball.check_edges_vertical():
            change_ball_direction_vertical(ai_settings, balls)
            break


def check_right_paddle_edges(ai_settings, right_paddle):
    if right_paddle.check_edges():
        right_paddle.rect.y += ai_settings.right_paddle_speed_factor
        ai_settings.right_paddle_y_direction *= -1


def change_ball_direction_horizontal(ai_settings, balls):
    """Change ball direction left and right."""
    for ball in balls.sprites():
        ball.rect.x += ai_settings.ball_speed_factor
    ai_settings.ball_x_direction *= -1


def change_ball_direction_vertical(ai_settings, balls):
    """Change ball direction up and down."""
    for ball in balls.sprites():
        ball.rect.y -= ai_settings.ball_speed_factor
    ai_settings.ball_y_direction *= -1


def update_right_paddle(ai_settings, right_paddle):
    check_right_paddle_edges(ai_settings, right_paddle)


def update_balls(ai_settings, stats, screen, sb, left_paddle, right_paddle, balls):
    """Update position of balls and get rid of old balls."""
    pygame.init()
    balls.update(ai_settings)
    for ball in balls.copy():
        """Events when ball collides with something."""
        # Ball hits paddle
        if ball.collision_left_right(left_paddle, right_paddle):
            pygame.mixer.music.load("sounds/ping_pong_8bit_plop.wav")
            pygame.mixer_music.play(1)
            change_ball_direction_horizontal(ai_settings, balls)
        # Ball hits top or bottom of screen
        if ball.rect.bottom <= 0 or ball.rect.top >= ai_settings.screen_height:
            change_ball_direction_vertical(ai_settings, balls)
            pygame.mixer.music.load("sounds/ping_pong_8bit_beeep.wav")
            pygame.mixer_music.play(1)
        # Cpu Scores
        elif ball.rect.left <= 0:
            stats.cpu_score += 1
            sb.prep_cpu_score()
            pygame.mixer.music.load("sounds/ping_pong_8bit_peeeeeep.wav")
            pygame.mixer_music.play(1)
            change_ball_direction_horizontal(ai_settings, balls)
            change_ball_direction_vertical(ai_settings, balls)
            ball.remove(balls)
        # Player scores
        elif ball.rect.right >= ai_settings.screen_width:
            stats.player_score += ai_settings.points
            sb.prep_player_score()
            pygame.mixer.music.load("sounds/ping_pong_8bit_peeeeeep.wav")
            pygame.mixer_music.play(1)
            change_ball_direction_horizontal(ai_settings, balls)
            change_ball_direction_vertical(ai_settings, balls)
            if stats.player_score > stats.high_score:
                stats.high_score = stats.player_score
                sb.prep_high_score()
            ball.remove(balls)


def update_screen(ai_settings, screen, stats, sb, left_paddle, right_paddle, balls, play_button):
    """Update the screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    left_paddle.draw_left_paddle()
    right_paddle.draw_right_paddle()
    sb.prep_mid_line()
    for ball in balls.sprites():
        ball.draw_ball()
    # Draw the score information.
    sb.show_score()
    # Draw the play button if the game is inactive.
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()
