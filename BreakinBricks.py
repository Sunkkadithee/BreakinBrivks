import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Breakin' Bricks")

# bat
bat = pygame.image.load('Images/paddle.png')
bat = bat.convert_alpha()
bat_rect = bat.get_rect()
bat_rect[1] = screen.get_height() - 100

# ball
ball = pygame.image.load('Images/football.png')
ball = ball.convert_alpha()
ball_rect = ball.get_rect()
ball_speed = (3.0, 3.0)
ball_served = False
sx, sy = ball_speed

# brick
brick = pygame.image.load('Images/brick.png')
brick = brick.convert_alpha()
brick_rect = brick.get_rect()
bricks = []
brick_rows = 5
brick_gap = 10
brick_cols = screen.get_width() // (brick_rect.width + brick_gap)
side_gap = (screen.get_width() - (brick_rect.width + brick_gap) * brick_cols + brick_gap) // 2

for y in range(brick_rows):
    brickY = y * (brick_rect.height + brick_gap)
    for x in range(brick_cols):
        brickX = x * (brick_rect.width + brick_gap) + side_gap
        bricks.append((brickX, brickY))

clock = pygame.time.Clock()
game_over = False
x = bat_rect[0]

while not game_over:
    dt = clock.tick(50)
    screen.fill((0, 0, 0))

    for b in bricks:
        screen.blit(brick, b)

    # Show on screen
    screen.blit(bat, bat_rect)
    screen.blit(ball, ball_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEMOTION:  # Mouse movement
            x, _ = event.pos
            x -= bat_rect.width // 2  # Center the bat on the mouse

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_RIGHT]:
        x += 0.5 * dt
    if pressed_keys[K_LEFT]:
        x -= 0.5 * dt
    if pressed_keys[K_SPACE]:
        ball_served = True

    # Bat collision
    if bat_rect.colliderect(ball_rect) and sy > 0:
        sy *= -1
        sx *= 1.01  # Increase difficulty
        sy *= 1.01

    # Brick collision
    delete_brick = None
    for b in bricks:
        bx, by = b
        if bx <= ball_rect[0] <= bx + brick_rect.width and \
                by <= ball_rect[1] <= by + brick_rect.height:
            delete_brick = b

            if ball_rect[0] <= bx + 2 or ball_rect[0] >= bx + brick_rect.width - 2:
                sx *= -1
            if ball_rect[1] <= by + 2 or ball_rect[1] >= by + brick_rect.height - 2:
                sy *= -1
            break
    if delete_brick is not None:
        bricks.remove(delete_brick)

    # Ball screen collision
    if ball_rect[1] <= 0:
        ball_rect[1] = 0
        sy *= -1
    if ball_rect[1] >= screen.get_height() - ball_rect.height:
        ball_served = False
        ball_rect.topleft = (bat_rect[0] + bat_rect.width // 2 - ball_rect.width // 2, bat_rect[1] - ball_rect.height)
        sx, sy = ball_speed  # Reset speed
    if ball_rect[0] <= 0:
        ball_rect[0] = 0
        sx *= -1
    if ball_rect[0] >= screen.get_width() - ball_rect.width:
        ball_rect[0] = screen.get_width() - ball_rect.width
        sx *= -1

    # Restrict the bat's movement within the screen
    if x < 0:
        x = 0
    elif x > screen.get_width() - bat_rect.width:
        x = screen.get_width() - bat_rect.width

    bat_rect[0] = x  # Update the bat position

    # Position the ball on the bat if not served
    if not ball_served:
        ball_rect.topleft = (bat_rect[0] + bat_rect.width // 2 - ball_rect.width // 2, bat_rect[1] - ball_rect.height)
    else:
        ball_rect[0] += sx
        ball_rect[1] += sy

    pygame.display.update()

pygame.quit()
