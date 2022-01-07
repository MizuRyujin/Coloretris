# Import pygame into our program
import pygame
# Import pygame font module
import pygame.freetype
# Import random into our program
import random

# Initialize pygame, with the default parameters
pygame.init()

# Define the size/resolution of our window
res = (640, 360)

# Create a window and display surface
screen = pygame.display.set_mode(res)

# Retrieve the ammount of time since pygame.init() was called
last_time = pygame.time.get_ticks()

font = pygame.freetype.Font("Aulas/Assets/NotoSans-Regular.ttf", 24)

# Load image
ball_blue = pygame.image.load("Aulas/Assets/EggBlue.png")
ball_size = ball_blue.get_size()

x = random.randint(0, res[0] - ball_blue.get_width())
y = random.randint(0, res[1] - ball_blue.get_height())
vx = 150
vy = 75

bounce_counter = 0

while True:
    # Process system events
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            exit()

    # Compute elapsed time in seconds
    elapsed_time = (pygame.time.get_ticks() - last_time) / 1000

    # Update time stamp
    last_time = pygame.time.get_ticks()

    # Clears the screen to black
    screen.fill((64, 0, 64))

    x = x + vx * elapsed_time
    y = y + vy * elapsed_time

    if (x > res[0] - ball_size[0]) and (vx > 0):
        vx = -vx
        bounce_counter += 1
    elif (x < 0) and (vx < 0):
        vx = -vx
        bounce_counter += 1

    if (y > res[1] - ball_size[1]) and (vy > 0):
        vy = -vy
        bounce_counter += 1
    elif (y < 0) and (vy < 0):
        vy = -vy
        bounce_counter += 1

    # Draw ball
    screen.blit(ball_blue, (x, y))
    font.render_to(screen, (20, 20), str(bounce_counter), (255, 255, 0))

    # Swaps the back and front buffer, effectively displaying what we rendered
    pygame.display.flip()
