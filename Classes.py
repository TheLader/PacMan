import pygame
from pygame.locals import *
class GameObject:
    Position = None
    Image = None
    ColliderRect = None

    def SpawnObject(self):
        self.Position = 1

    def DestroyObject(self):
        self.Position = 1


class Entity(GameObject):
    HealthPoint = None
    def Movement(self):
        HealthPoint = self.HealthPoint

class Player(Entity):
    def __init__(self, Position, Image, ColliderRect):
        self.Image = pygame.image.load(Image)
        self.Image = pygame.transform.scale(self.Image, ColliderRect)
        self.Position = Position

    def Movement(self):
        keys = pygame.key.get_pressed()
        if keys[K_w]:
            self.Position = (self.Position[0], self.Position[1]-10)
        if keys[K_a]:
            self.Position = (self.Position[0]-10, self.Position[1])
        if keys[K_s]:
            self.Position = (self.Position[0], self.Position[1]+10)
        if keys[K_d]:
            self.Position = (self.Position[0]+10, self.Position[1])




class Enemy(Entity):
    IQ = None


class WorldObject(GameObject):
    Coordinates = None


class Wall(WorldObject):
    def __init__(self, Coordinates, Image, ColliderRect):
        # Завантаження та зміна розміру зображення
        self.Image = pygame.image.load(Image)
        self.Image = pygame.transform.scale(self.Image, ColliderRect)

        # Обчислення позиції
        self.Position = (Coordinates[0] * ColliderRect[0], Coordinates[1] * ColliderRect[1])


class Food(WorldObject):
    def __init__(self, Coordinates, Image, ColliderRect):
        # Завантаження та зміна розміру зображення
        self.Image = pygame.image.load(Image)
        self.Image = pygame.transform.scale(self.Image, ColliderRect)

        # Обчислення позиції
        self.Position = (Coordinates[0] * ColliderRect[0], Coordinates[1] * ColliderRect[1])


