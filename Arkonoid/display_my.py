import pygame
from random import randrange as rnd
from colision import *
class display():
    WIDTH, HEIGHT = 1200, 800
    fps = 60
    # Настройки ракетки
    paddle_w = 330
    paddle_h = 35
    paddle_speed = 15
    paddle = pygame.Rect(WIDTH // 2 - paddle_w // 2, HEIGHT - paddle_h - 10, paddle_w, paddle_h)
    # Настройки шарика
    ball_radius = 20
    ball_speed = 6
    ball_rect = int(ball_radius * 2 ** 0.5)
    ball = pygame.Rect(rnd(ball_rect, WIDTH - ball_rect), HEIGHT // 2, ball_rect, ball_rect)
    dx, dy = 1, -1
    # Настройки блоков
    block_list = [pygame.Rect(10 + 120 * i, 10 + 70 * j, 100, 50) for i in range(10) for j in range(4)]
    color_list = [(rnd(30, 256), rnd(30, 256), rnd(30, 256)) for i in range(10) for j in range(4)]

    pygame.init()
    sc = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    
    # Задний фон
    img = pygame.image.load('1.jpg').convert()
    
class reload_display_game():
    def reload_display():
        # Обновление дисплея
        pygame.display.flip()
        display.clock.tick(display.fps)

class gameplay_arko():
    def gameplay():
        # Создание окружения
        [pygame.draw.rect(display.sc, display.color_list[color], block) for color, block in enumerate(display.block_list)]
        pygame.draw.rect(display.sc, pygame.Color('darkorange'), display.paddle)
        pygame.draw.circle(display.sc, pygame.Color('white'), display.ball.center, display.ball_radius)
        # Движение шара
        display.ball.x += display.ball_speed * display.dx
        display.ball.y += display.ball_speed * display.dy
        # Колизия вправа, влево
        if display.ball.centerx < display.ball_radius or display.ball.centerx > display.WIDTH - display.ball_radius:
            display.dx = -display.dx
        # Колизия верха
        if display.ball.centery < display.ball_radius:
            display.dy = -display.dy
        # Колизия отбивающей поверхности
        if display.ball.colliderect(display.paddle) and display.dy > 0:
            display.dx, display.dy = colision.detect_collision(display.dx, display.dy, display.ball, display.paddle)
        # Колизия блоков
        hit_index = display.ball.collidelist(display.block_list)
        if hit_index != -1:
            hit_rect = display.block_list.pop(hit_index)
            hit_color = display.color_list.pop(hit_index)
            display.dx, display.dy = colision.detect_collision(display.dx, display.dy, display.ball, hit_rect)
            # Специальные эфекты
            hit_rect.inflate_ip(display.ball.width * 3, display.ball.height * 3)
            pygame.draw.rect(display.sc, hit_color, hit_rect)
            display.fps += 2

class control():
    def control_game():
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and display.paddle.left > 0:
            display.paddle.left -= display.paddle_speed
        if key[pygame.K_RIGHT] and display.paddle.right < display.WIDTH:
            display.paddle.right += display.paddle_speed

class win_game_over():
    def game_result():
        if display.ball.bottom > display.HEIGHT:
            print('GAME OVER!')
            exit()
        elif not len(display.block_list):
            print('WIN!!!')
            exit()