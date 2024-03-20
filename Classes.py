import pygame
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


class Player(Entity):
    def __init__(self, Position, Image, ColliderRect):
        self.Position = Position
        self.Image = Image
        self.ColliderRect = ColliderRect



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
    Color = None
