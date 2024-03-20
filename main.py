
import numpy as np
import Classes
import world

import pygame
import sys

# Initialize Pygame
pygame.init()
objects = []
# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Template")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

wall = Classes.Wall((4,0), "Images\\wall.jpg", (50,50))
wall1 = Classes.Wall((5,0), "Images\\wall.jpg", (50,50))
objects.append(wall)
objects.append(wall1)
#Player = Classes.Player((10, 10), pygame.image.load("Images\\бугров.png"), (50, 50))
#Object = Classes.GameObject


# Game loop
clock = pygame.time.Clock()
is_running = True

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    # Update
    # Draw
    screen.fill(WHITE)
    world.DrawingWorldWalls(screen)
    #screen.blit(wall.Image, wall.Position)
    #screen.blit(Player.Image, Player.Position)
    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()

