import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_SPEED = 5
PADDLE_SPEED = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

# Initialize ball position and speed
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_speed_x = random.choice((BALL_SPEED, -BALL_SPEED))
ball_speed_y = random.choice((BALL_SPEED, -BALL_SPEED))

# Initialize paddle positions
left_paddle_y = (HEIGHT - 100) // 2
right_paddle_y = (HEIGHT - 100) // 2

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle_y > 0:
        left_paddle_y -= PADDLE_SPEED
    if keys[pygame.K_s] and left_paddle_y < HEIGHT - 100:
        left_paddle_y += PADDLE_SPEED
    if keys[pygame.K_UP] and right_paddle_y > 0:
        right_paddle_y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and right_paddle_y < HEIGHT - 100:
        right_paddle_y += PADDLE_SPEED

    # Move ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with top and bottom walls
    if ball_y <= 0 or ball_y >= HEIGHT - 20:
        ball_speed_y = -ball_speed_y

    # Ball collision with paddles
    if (
        ball_x <= 20
        and left_paddle_y <= ball_y <= left_paddle_y + 100
        or ball_x >= WIDTH - 40
        and right_paddle_y <= ball_y <= right_paddle_y + 100
    ):
        ball_speed_x = -ball_speed_x

    # Ball out of bounds (score point)
    if ball_x < 0 or ball_x > WIDTH:
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_speed_x = random.choice((BALL_SPEED, -BALL_SPEED))
        ball_speed_y = random.choice((BALL_SPEED, -BALL_SPEED))

    # Clear the screen
    screen.fill(BLACK)

    # Draw paddles and ball
    pygame.draw.rect(screen, WHITE, (20, left_paddle_y, 20, 100))
    pygame.draw.rect(screen, WHITE, (WIDTH - 40, right_paddle_y, 20, 100))
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, 20, 20))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
