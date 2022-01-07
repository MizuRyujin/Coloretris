# Import pygame into our program
import pygame
import random

positions = []
res = (640, 360)

for i in range(0, 300):
    x = random.randint(0, res[0])
    y = random.randint(res[1] / 2, res[1])
    positions.append((x, y))


# Initialize pygame, with the default parameters
pygame.init()

# Define the size/resolution of our window

# Create a window and display surface
screen = pygame.display.set_mode(res)

# Retrieve the ammount of time since pygame.init() was called
last_time = pygame.time.get_ticks()

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
    screen.fill((0, 255, 200))

    # Draw code here
    pygame.draw.circle(screen, (255, 255, 0), (50, 50), 20)
    pygame.draw.polygon(screen, (128, 128, 128), [
                        (0, 200), (70, 100), (250, 130), (320, 50), (440, 150), (640, 200)])
    pygame.draw.rect(screen, (150, 75, 0), (0, res[1]/2, 1000, 1000))

    for x, y in positions:
        pygame.draw.line(screen, (0, 125, 0), (x, y), (x + 5, y - 5),3)
    # Swaps the back and front buffer, effectively displaying what we rendered
    pygame.display.flip()
