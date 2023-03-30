import pygame
from display_my import *
from colision import *
from ai_player import *

player_vs_AI = False
AI_vs_AI = True

if player_vs_AI == True:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        display.sc.blit(display.img, (0, 0))
        game = gameplay_arko.gameplay()
        # Победа или проигрыш
        score_game = win_game_over.game_result()
        # Контроль
        contols = control.control_game()
        # Обновление дисплея
        reload_display_game_arko = reload_display_game.reload_display()

elif AI_vs_AI == True:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        display.sc.blit(display.img, (0, 0))
        game = gameplay_arko.gameplay()
        ai_play_game = ai_game.ai_player()
        # Победа или проигрышь
        score_game = win_game_over.game_result()
        # Контроль
        contols = control.control_game()
        # Обновление дисплея
        reload_display_game_arko = reload_display_game.reload_display()