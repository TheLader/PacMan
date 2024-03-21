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
def setWorld():
    for y, row in enumerate(world):
        for x, cell in enumerate(row):
            if cell == 1:  # Якщо в масиві 1, малюємо стіну
                wall_position = (x ,y )  # Позиція стіни на екрані
                walls.append(Classes.Wall(wall_position, wallImagePath, (50, 50)))  # Додаємо стіну до списку
def DrawingWorldWalls(screen):
    for wall in walls:
        screen.blit(wall.Image, wall.Position)

foodMap = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
          [1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
          [1,0,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,0,1],
          [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1],
          [1,0,1,0,1,1,0,1,1,2,2,1,1,0,1,1,0,1,0,1],
          [1,0,0,0,0,0,0,1,2,2,2,2,1,0,0,0,0,0,0,1],
          [1,0,1,0,1,1,0,1,1,1,1,1,1,0,1,1,0,1,0,1],
          [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1],
          [1,0,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,0,1],
          [1,0,0,0,0,1,0,0,0,2,2,0,0,0,1,0,0,0,0,1],
          [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
foodImagePath = "images\\food.png"
foods = []
def setFood():
    for y, row in enumerate(foodMap):
        for x, cell in enumerate(row):
            if cell == 0:  # Якщо в масиві 0, малюємо їжу
                food_position = (x ,y )  # Позиція їжі на екрані
                foods.append(Classes.Food(food_position, foodImagePath, (50, 50)))  # Додаємо їжу до списку
def DrawingWorldFood(screen):
    for food in foods:
        screen.blit(food.Image, food.ColliderRect)