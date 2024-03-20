import pygame
import Classes
wall = Classes.Wall((4,0), "Images\\wall.jpg", (50,50))
world = [[1,1,1],[1,0,1],[1,1,1]]
def DrawingWorldWalls(screen):
    for y, row in enumerate(world):
        for x, cell in enumerate(row):
            if cell == 1:  # Якщо в масиві 1, малюємо стіну
                screen.blit(wall.Image, (x * 50, y * 50))  # Виводимо стіну на екран у відповідному місці