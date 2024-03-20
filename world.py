import pygame
import Classes
world = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
         [1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
         [1,0,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,0,1],
         [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1],
         [1,0,1,0,1,1,0,1,1,0,0,1,1,0,1,1,0,1,0,1],
         [1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1],
         [1,0,1,0,1,1,0,1,1,1,1,1,1,0,1,1,0,1,0,1],
         [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1],
         [1,0,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,0,1],
         [1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
worldLenght = len(world)
worldWidth= len(world[0])
# Список стін
walls = []
wallImagePath = "Images\\wall.jpg"
def DrawingWorldWalls(screen):
    for y, row in enumerate(world):
        for x, cell in enumerate(row):
            if cell == 1:  # Якщо в масиві 1, малюємо стіну
                wall_position = (x ,y )  # Позиція стіни на екрані
                walls.append(Classes.Wall(wall_position, wallImagePath, (50, 50)))  # Додаємо стіну до списку
    for wall in walls:
        screen.blit(wall.Image, wall.Position)