import pygame, sys
from game import Game
from colors import Colors

pygame.init()

# Display settings
title_font = pygame.font.Font(None, 80)
text_font = pygame.font.Font(None, 40)

title_surface = title_font.render("Python TETRIS", True, Colors.white)
press_enter_surface = text_font.render("PRESS ENTER", True, Colors.white)
score_surface = text_font.render("Score", True, Colors.white)
next_surface = text_font.render("Next", True, Colors.white)
game_over_surface = text_font.render("GAME OVER", True, Colors.white)

score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 415, 170, 180)

# Screen setting
screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Python Tetris")
clock = pygame.time.Clock()

# Game logic
game = Game()
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 600)
game_state = "title"

# Print grid for debugging
# game_grid.print_grid()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            # Title screen
            if game_state == "title":
                if event.key == pygame.K_RETURN:
                    game_state = "playing"
            # Game over screen
            elif game_state == "game_over":
                if event.key == pygame.K_RETURN:
                    game.game_over = False
                    game.reset()
                    game_state = "playing"
            # Game screen
            elif game_state == "playing":
                # Move blocks
                if event.key == pygame.K_LEFT and game.game_over == False:
                    game.move_left()
                if event.key == pygame.K_RIGHT and game.game_over == False:
                    game.move_right()
                if event.key == pygame.K_DOWN and game.game_over == False:
                    game.move_down()
                    game.update_score(0, 1)
                # Rotate blocks
                if event.key == pygame.K_UP or event.key == pygame.K_SPACE and game.game_over == False:
                    game.rotate()
        # Block fall
        if event.type == GAME_UPDATE and game_state == "playing" and not game.game_over:
            game.move_down()

    # Draw
    screen.fill(Colors.dark_grey)

    # Draw title screen
    if game_state == "title":
        title_rect = title_surface.get_rect(center=(screen.get_width() / 2, 250))
        press_enter_rect = press_enter_surface.get_rect(center=(screen.get_width() / 2, 350))

        screen.blit(title_surface, title_rect)
        screen.blit(press_enter_surface, press_enter_rect)

    # Draw game screen
    elif game_state == "playing":
        score_value_surface = text_font.render(str(game.score), True, Colors.white)
        screen.blit(score_surface, (365, 20, 50, 50))
        screen.blit(next_surface, (375, 380, 50, 50))
        pygame.draw.rect(screen, Colors.black, score_rect, 0, 10)
        screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, centery = score_rect.centery))
        pygame.draw.rect(screen, Colors.black, next_rect, 0, 10)
        game.draw(screen)
        # Game over
        if game.game_over == True:
            screen.blit(game_over_surface, (80, 300, 50, 50))
            game_state = "game_over"

    # Update
    pygame.display.update()
    clock.tick(60)