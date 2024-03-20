
import numpy as np
import Classes
import world

import pygame
import sys

# Initialize Pygame
pygame.init()
objects = []
# Set up display
WIDTH, HEIGHT = world.worldWidth*50, world.worldLenght*50
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Template")
world.setWorld()
Player = Classes.Player((10,10), "Images\\PacMan.jpg",(50,50))
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game loop
clock = pygame.time.Clock()
is_running = True

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    # Update
    Player.Movement()
    # Draw
    screen.fill(BLACK)
    world.DrawingWorldWalls(screen)
    #screen.blit(wall.Image, wall.Position)
    screen.blit(Player.Image, Player.Position)
    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()

