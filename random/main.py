# Darius Corbin
# 01/28/2023
# Bouncing DVD animation

# Install pygam 'p install pygame'

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# Define the speed and direction of the letter movement
SPEED = 5
dx = SPEED
dy = SPEED

pygame.init()

# Set the screen dimensions and title
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Bouncing DVD Logo")

# Load the font
font = pygame.font.SysFont('arial', 100)

# Create the "DVD" surface
dvd_surf = font.render('DVD', True, GREEN)

# Set the initial position of the "DVD" surface
dvd_rect = dvd_surf.get_rect()
dvd_rect.centerx = random.randint(dvd_rect.width // 2, SCREEN_WIDTH - dvd_rect.width // 2)
dvd_rect.centery = random.randint(dvd_rect.height // 2, SCREEN_HEIGHT - dvd_rect.height // 2)

# Run until the user asks to quit
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Main loop
while not done:
    # --- Event Processing ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game Logic ---

    # Move the "DVD" surface
    dvd_rect.x += dx
    dvd_rect.y += dy

    # Bounce the "DVD" surface off the walls
    if dvd_rect.left < 0 or dvd_rect.right > SCREEN_WIDTH:
        dx = -dx
        dvd_surf = pygame.transform.flip(dvd_surf, True, False)
    if dvd_rect.top < 0 or dvd_rect.bottom > SCREEN_HEIGHT:
        dy = -dy
        dvd_surf = pygame.transform.flip(dvd_surf, False, True)

    # --- Drawing ---
    # Set the screen background
    screen.fill(BLACK)

    # Draw the "DVD" surface
    screen.blit(dvd_surf, dvd_rect)

    # --- Update the screen ---
    pygame.display.update()

    # --- Clock tick ---
    clock.tick(60)

# Close the window and quit.
pygame.quit()
