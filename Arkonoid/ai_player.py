import pygame
from display_my import *
from colision import *

class ai_game():
    def ai_player():
        if display.ball.centerx < display.paddle.left:
            display.paddle.move_ip(-display.paddle_speed, 0)
        elif display.ball.centerx > display.paddle.right:
            display.paddle.move_ip(display.paddle_speed, 0)