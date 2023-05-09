import pygame
import sys
import random
from pygame.locals import *

# Khởi tạo
pygame.init()
fps = pygame.time.Clock()

# Cấu hình
WINDOW_SIZE = (800, 600)
GRID_SIZE = 20
GRID_WIDTH = WINDOW_SIZE[0] // GRID_SIZE
GRID_HEIGHT = WINDOW_SIZE[1] // GRID_SIZE
SNAKE_SIZE = GRID_SIZE
SNAKE_SPEED = GRID_SIZE
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Tạo cửa sổ
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Rắn săn mồi")


def draw_grid():
    for x in range(0, WINDOW_SIZE[0], GRID_SIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, WINDOW_SIZE[1]))
    for y in range(0, WINDOW_SIZE[1], GRID_SIZE):
        pygame.draw.line(screen, BLACK, (0, y), (WINDOW_SIZE[0], y))


def random_food_position():
    return (
        random.randint(0, GRID_WIDTH - 1) * GRID_SIZE,
        random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE
    )


def draw_score(score):
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, BLACK)
    text_rect = text.get_rect()
    text_rect.topleft = (10, 10)
    screen.blit(text, text_rect)


def random_snake_position():
    return (
        random.randint(3, GRID_WIDTH - 4) * GRID_SIZE,
        random.randint(3, GRID_HEIGHT - 4) * GRID_SIZE
    )


def game_over():
    font = pygame.font.Font(None, 54)
    text = font.render("Game Over!", True, RED)
    text_rect = text.get_rect()
    text_rect.center = (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2)
    screen.blit(text, text_rect)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                main()


def main():
    # Vị trí rắn và mồi
    head = random_snake_position()
    snake = [head, (head[0] - SNAKE_SIZE, head[1]),
             (head[0] - 2 * SNAKE_SIZE, head[1])]
    snake_direction = (SNAKE_SPEED, 0)
    new_direction = snake_direction
    food = random_food_position()

    # Khởi tạo điểm số
    score = 0

    moved = True

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # Kiểm soát rắn
            if event.type == KEYDOWN and moved:
                if event.key == K_UP and snake_direction[1] != SNAKE_SPEED:
                    new_direction = (0, -SNAKE_SPEED)
                elif event.key == K_DOWN and snake_direction[1] != -SNAKE_SPEED:
                    new_direction = (0, SNAKE_SPEED)
                elif event.key == K_LEFT and snake_direction[0] != SNAKE_SPEED:
                    new_direction = (-SNAKE_SPEED, 0)
                elif event.key == K_RIGHT and snake_direction[0] != -SNAKE_SPEED:
                    new_direction = (SNAKE_SPEED, 0)
                moved = False
        
        # Cập nhật vị trí rắn
        snake_direction = new_direction
        new_head = (snake[0][0] + snake_direction[0],
                    snake[0][1] + snake_direction[1])

        if (new_head[0] < 0 or new_head[0] >= WINDOW_SIZE[0]
                or new_head[1] < 0 or new_head[1] >= WINDOW_SIZE[1]
                or new_head in snake[1:]):
            game_over()

        snake.insert(0, new_head)

        # Kiểm tra ăn mồi
        if new_head == food:
            food = random_food_position()
            # Cập nhật điểm số
            score += 1
        else:
            snake.pop()

        # Vẽ rắn và mồi
        screen.fill(WHITE)
        for s in snake:
            pygame.draw.rect(
                screen, GREEN, (s[0], s[1], SNAKE_SIZE, SNAKE_SIZE))
        pygame.draw.rect(
            screen, RED, (food[0], food[1], SNAKE_SIZE, SNAKE_SIZE))

        draw_grid()
        draw_score(score)  # Hiển thị điểm số

        pygame.display.flip()
        fps.tick(7)
        moved = True

if __name__ == "__main__":
    main()
