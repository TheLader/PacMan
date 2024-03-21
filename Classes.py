import pygame
from pygame.locals import *
class GameObject:
    Position = None
    OriginalImage = None
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
        self.OriginalImage = pygame.image.load(Image)
        self.OriginalImage = pygame.transform.scale(self.OriginalImage, ColliderRect)
        self.Position = (Position[0] * 50, Position[1] * 50)
        self.Image = self.OriginalImage
        self.ColliderRect = self.Image.get_rect()
        self.angle = 0


    def Movement(self):
        keys = pygame.key.get_pressed()

        if keys[K_w]:
            self.Position = (self.Position[0], self.Position[1]-5)
            self.Image = pygame.transform.rotate(self.OriginalImage, 270)
        if keys[K_a]:
            self.Position = (self.Position[0]-5, self.Position[1])
            self.Image = pygame.transform.rotate(self.OriginalImage, 0)
        if keys[K_s]:
            self.Position = (self.Position[0], self.Position[1]+5)
            self.Image = pygame.transform.rotate(self.OriginalImage, 90)
        if keys[K_d]:
            self.Position = (self.Position[0]+5, self.Position[1])
            self.Image = pygame.transform.rotate(self.OriginalImage, 180)
        self.ColliderRect.x = self.Position[0]
        self.ColliderRect.y = self.Position[1]




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
        self.ColliderRect = self.Image.get_rect()
        # Обчислення позиції
        self.Position = (Coordinates[0] * ColliderRect[0], Coordinates[1] * ColliderRect[1])
        self.ColliderRect.x = self.Position[0]
        self.ColliderRect.y = self.Position[1]
class UI(GameObject):
    def __init__(self, font, position=(30, 560), color=(255, 255, 255)):
        self.Position = position
        self.font = font
        self.color = color
        self.score = 0

    def update_score(self, new_score):
        self.score = new_score

    def draw(self, screen):
        score_text = self.font.render(f"Score: {self.score}", True, self.color)
        screen.blit(score_text, self.Position)