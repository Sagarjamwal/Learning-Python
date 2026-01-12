import pygame
import sys
import random
pygame.init()

# Settings
WIDTH, HEIGHT = 600, 600
BLOCK_SIZE = 20
SPEED = 15
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Final Snake Game")
clock = pygame.time.Clock()

font_style = pygame.font.SysFont("bahnschrift", 25)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    text_rect = mesg.get_rect(center=(WIDTH/2, HEIGHT/2))
    screen.blit(mesg, text_rect)

def gameLoop():
    game_over = False
    game_close = False

    # Starting Position
    x = WIDTH / 2
    y = HEIGHT / 2
    x_change = 0
    y_change = 0

    snake_list = []
    snake_length = 1

    # Place first food
    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 20.0) * 20.0
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 20.0) * 20.0

    while not game_over:

        # --- A. GAME OVER SCREEN ---
        while game_close == True:
            screen.fill(BLACK)
            message("You Lost! Press Q-Quit or C-Play Again", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # CONTROLS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_change == 0:
                    x_change = -BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_RIGHT and x_change == 0:
                    x_change = BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_UP and y_change == 0:
                    y_change = -BLOCK_SIZE
                    x_change = 0
                elif event.key == pygame.K_DOWN and y_change == 0:
                    y_change = BLOCK_SIZE
                    x_change = 0

        # CHECK BOUNDARIES
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True
        
        # D. MOVE SNAKE 
        x += x_change
        y += y_change
        
        screen.fill(BLACK)
        
        # Draw Food
        pygame.draw.rect(screen, GREEN, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])
        
        # Update Snake Body
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        
        if len(snake_list) > snake_length:
            del snake_list[0]

        #E. CHECK TAIL COLLISION 
        for x_coord in snake_list[:-1]:
            if x_coord == snake_head:
                game_close = True

        # Draw Snake
        for block in snake_list:
            pygame.draw.rect(screen, WHITE, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])

        pygame.display.update()

        # F. EATING FOOD
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 20.0) * 20.0
            food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 20.0) * 20.0
            snake_length += 1

        clock.tick(SPEED)

    pygame.quit()
    sys.exit()

gameLoop()