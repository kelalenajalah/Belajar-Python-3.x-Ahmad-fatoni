import pygame
import random
import math

pygame.init()

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Extreme Puzzle Game: Matriks & Sudut Melengkung")

WHITE = (255, 255, 255)
ORANGE = (255, 120, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
GRAY = (100, 100, 100)
YELLOW = (255, 255, 0)

x = 10
y = 10
RECT_WIDTH = 10
RECT_HEIGHT = 10
SPEED = 5
BORDER_RADIUS = 3

obstacles = [
    (50, 50, 400, 10),
    (50, 50, 10, 400),
    (440, 50, 10, 400),
    (50, 440, 400, 10),
    (100, 100, 10, 300),
    (200, 100, 250, 10),
    (200, 200, 10, 200),
    (300, 100, 10, 300),
    (100, 300, 200, 10),
    (350, 50, 10, 350),
    (150, 150, 50, 10),
    (250, 250, 50, 10),
    (350, 150, 50, 10),
]

moving_obstacles = [
    (150, 70, 20, 20, 2, 0, 150, 280, 70, 70),
    (70, 150, 20, 20, 0, 2, 70, 70, 150, 280),
    (320, 320, 20, 20, 2, 2, 320, 400, 320, 400),
]

fake_walls = [
    (250, 100, 50, 10),
]

traps = [
    (120, 120, 20, 20),
    (320, 280, 20, 20),
]

keys = [
    (80, 80, 10, 10),
    (420, 80, 10, 10),
    (420, 420, 10, 10),
]

matrix_problems = [
    ([[2, 1], [0, 3]], [[1, 0], [2, 1]], [[4, 1], [6, 3]], [([[3, 1], [2, 3]], 10), ([[4, 1], [6, 3]], 0), ([[2, 1], [0, 3]], 10)]),
    ([[1, 2], [3, 0]], [[0, 1], [1, 2]], [[2, 5], [3, 6]], [([[2, 5], [3, 6]], 0), ([[1, 2], [3, 0]], 10), ([[0, 1], [2, 3]], 10)]),
    ([[3, 0], [1, 2]], [[2, 1], [0, 1]], [[6, 3], [2, 3]], [([[1, 1], [2, 2]], 10), ([[6, 3], [2, 3]], 0), ([[3, 0], [1, 2]], 10)]),
]

answer_positions = [
    (100, 450, 50, 20),
    (200, 450, 50, 20),
    (300, 450, 50, 20),
]

exit_rect = (WINDOW_WIDTH - 20, WINDOW_HEIGHT - 20, 10, 10)

font = pygame.font.SysFont("arial", 18)

is_running = True
game_won = False
game_over = False
keys_collected = 0
max_keys = len(keys)
current_problem = 0
max_steps = 100
steps_left = max_steps
max_time = 60 * 1000
start_time = pygame.time.get_ticks()

clock = pygame.time.Clock()
FPS = 60

while is_running:
    clock.tick(FPS)

    elapsed_time = pygame.time.get_ticks() - start_time
    time_left = max(0, (max_time - elapsed_time) // 1000)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    if not game_won and not game_over:
        keys_pressed = pygame.key.get_pressed()
        prev_x, prev_y = x, y

        if keys_pressed[pygame.K_LEFT] and x > 0:
            x -= SPEED
            steps_left -= 1
        if keys_pressed[pygame.K_RIGHT] and x < WINDOW_WIDTH - RECT_WIDTH:
            x += SPEED
            steps_left -= 1
        if keys_pressed[pygame.K_UP] and y > 0:
            y -= SPEED
            steps_left -= 1
        if keys_pressed[pygame.K_DOWN] and y < WINDOW_HEIGHT - RECT_HEIGHT:
            y += SPEED
            steps_left -= 1

        player_rect = pygame.Rect(x, y, RECT_WIDTH, RECT_HEIGHT)

        for obs in obstacles:
            if player_rect.colliderect(pygame.Rect(obs)):
                x, y = prev_x, prev_y
                break

        for i, (mx, my, mw, mh, sx, sy, min_x, max_x, min_y, max_y) in enumerate(moving_obstacles):
            mx += sx
            my += sy
            if mx <= min_x or mx >= max_x:
                sx = -sx
            if my <= min_y or my >= max_y:
                sy = -sy
            moving_obstacles[i] = (mx, my, mw, mh, sx, sy, min_x, max_x, min_y, max_y)
            if player_rect.colliderect(pygame.Rect((mx, my, mw, mh))):
                game_over = True

        for trap in traps:
            if player_rect.colliderect(pygame.Rect(trap)):
                game_over = True

        new_keys = []
        for i, key in enumerate(keys):
            if player_rect.colliderect(pygame.Rect(key)) and i == current_problem:
                for j, (ans, penalty) in enumerate(matrix_problems[current_problem][3]):
                    if player_rect.colliderect(pygame.Rect(answer_positions[j])):
                        if penalty == 0:
                            keys_collected += 1
                            current_problem += 1
                        else:
                            steps_left -= penalty
                        break
            else:
                new_keys.append(key)
        keys = new_keys

        if keys_collected == max_keys:
            exit_rect_obj = pygame.Rect(exit_rect)
            if player_rect.colliderect(exit_rect_obj):
                game_won = True

        if steps_left <= 0 or time_left <= 0:
            game_over = True

    window.fill(WHITE)

    for obs in obstacles:
        pygame.draw.rect(window, RED, obs, border_radius=BORDER_RADIUS)

    for (mx, my, mw, mh, _, _, _, _, _, _) in moving_obstacles:
        pygame.draw.rect(window, RED, (mx, my, mw, mh), border_radius=BORDER_RADIUS)

    for fw in fake_walls:
        pygame.draw.rect(window, GRAY, fw, border_radius=BORDER_RADIUS)

    for trap in traps:
        pygame.draw.rect(window, PURPLE, trap, border_radius=BORDER_RADIUS)

    for key in keys:
        pygame.draw.rect(window, BLUE, key, border_radius=BORDER_RADIUS)

    for i, (ans, _) in enumerate(matrix_problems[current_problem][3]):
        pygame.draw.rect(window, YELLOW, answer_positions[i], border_radius=BORDER_RADIUS)
        ans_text = font.render(str(ans), True, (0, 0, 0))
        window.blit(ans_text, (answer_positions[i][0] + 5, answer_positions[i][1] + 2))

    if keys_collected == max_keys:
        pygame.draw.rect(window, GREEN, exit_rect, border_radius=BORDER_RADIUS)

    pygame.draw.rect(window, ORANGE, (x, y, RECT_WIDTH, RECT_HEIGHT), border_radius=BORDER_RADIUS)

    steps_text = font.render(f"Steps: {steps_left}/{max_steps}", True, (0, 0, 0))
    time_text = font.render(f"Time: {time_left}s", True, (0, 0, 0))
    keys_text = font.render(f"Keys: {keys_collected}/{max_keys}", True, (0, 0, 0))
    window.blit(steps_text, (10, 10))
    window.blit(time_text, (10, 30))
    window.blit(keys_text, (10, 50))

    if current_problem < max_keys:
        m1, m2, correct, _ = matrix_problems[current_problem]
        matrix_text = font.render(f"[{m1[0]}][{m2[0]}] = [{correct[0]}]", True, (0, 0, 0))
        matrix_text2 = font.render(f"[{m1[1]}][{m2[1]}]   [{correct[1]}]", True, (0, 0, 0))
        window.blit(matrix_text, (350, 10))
        window.blit(matrix_text2, (350, 30))

    if game_won:
        win_text = font.render("You Win! IQ 200!", True, (0, 0, 255))
        window.blit(win_text, (WINDOW_WIDTH // 2 - 80, WINDOW_HEIGHT // 2 - 18))
    elif game_over:
        lose_text = font.render("Game Over!", True, (255, 0, 0))
        window.blit(lose_text, (WINDOW_WIDTH // 2 - 60, WINDOW_HEIGHT // 2 - 18))

    pygame.display.update()

pygame.quit()