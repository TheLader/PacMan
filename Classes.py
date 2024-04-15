import pygame
from pygame.locals import *
import sys
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
    def __init__(self, Position, Image, ColliderRect, max_health=3):
        self.OriginalImage = pygame.image.load(Image)
        self.OriginalImage = pygame.transform.scale(self.OriginalImage, ColliderRect)
        self.Position = (Position[0] * 50, Position[1] * 50)
        self.Image = self.OriginalImage
        self.ColliderRect = self.Image.get_rect()
        self.angle = 0
        self.MovementDirection = (1, 0)
        self.ChangeAngel(self.MovementDirection)
        self.NextMovementDirection = (0, 0)
        self.max_health = max_health
        self.health = max_health



    def Movement(self):
        keys = pygame.key.get_pressed()
        PlayerSpeed = 3
        if keys[K_w]:
            self.NextMovementDirection = (0, -1)
        if keys[K_a]:
            self.NextMovementDirection = (-1, 0)
        if keys[K_s]:
            self.NextMovementDirection = (0, 1)
        if keys[K_d]:
            self.NextMovementDirection = (1, 0)
        self.Position = (self.Position[0] + self.MovementDirection[0] * PlayerSpeed, self.Position[1] + self.MovementDirection[1] * PlayerSpeed)
        self.ColliderRect.x = self.Position[0]
        self.ColliderRect.y = self.Position[1]
    def ChangeAngel(self, Direction):
        if Direction == (0, -1):
            self.Image = pygame.transform.rotate(self.OriginalImage, 270)
        if Direction == (-1, 0):
            self.Image = pygame.transform.rotate(self.OriginalImage, 0)
        if Direction == (0, 1):
            self.Image = pygame.transform.rotate(self.OriginalImage, 90)
        if Direction == (1, 0):
            self.Image = pygame.transform.rotate(self.OriginalImage, 180)

    def lose_health(self, amount=1):
        self.health -= amount
        if self.health <= 0:
            # Додаткова логіка у випадку, якщо життя скінчилося
            print("Game Over!")  # Можна замінити на більш складну логіку, наприклад, перезавантаження гри або інше
            pygame.quit()
            sys.exit()


class Enemy(Entity):
    def __init__(self, Position, Image, ColliderRect, max_health=1):
        self.OriginalImage = pygame.image.load(Image)
        self.OriginalImage = pygame.transform.scale(self.OriginalImage, ColliderRect)
        self.Position = (Position[0] * 50, Position[1] * 50)
        self.Image = self.OriginalImage
        self.ColliderRect = self.Image.get_rect()
        self.ColliderRect.x = self.Position[0]
        self.ColliderRect.y = self.Position[1]
        self.angle = 0
        self.MovementDirection = (1, 0)
        self.NextMovementDirection = (0, 0)
        self.max_health = max_health
        self.health = max_health

    def Movement(self):
        # Implement enemy movement logic here
        pass

    # def lose_health(self, amount=1):
    #     super().lose_health(amount)
    #     # Additional logic specific to enemy health reduction
    #     pass


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
    def __init__(self, font, heart_image, position=(30, 560), color=(255, 255, 255)):
        self.Position = position
        self.font = font
        self.color = color
        self.score = 0
        self.health = 3
        self.heart_image = pygame.image.load(heart_image)
        self.heart_image = pygame.transform.scale(self.heart_image, (30, 30))

    def update_score(self, new_score):
        self.score = new_score

    def update_health(self, new_health):
        self.health = new_health

    def draw(self, screen):
        score_text = self.font.render(f"Score: {self.score}", True, self.color)
        screen.blit(score_text, self.Position)

        # Відображення сердечок
        for i in range(self.health):
            screen.blit(self.heart_image, (self.Position[0] + 810 + i * 40, self.Position[1]))

    def decrease_health(self):
        if self.health > 0:
            self.health -= 1



class MovementPoint(WorldObject):
    def __init__(self, Coordinates, Image, ColliderRect, MovementDirection):
        # Завантаження та зміна розміру зображення
        self.Image = pygame.image.load(Image)
        self.Image = pygame.transform.scale(self.Image, ColliderRect)
        self.Image.set_alpha(0)
        self.ColliderRect = self.Image.get_rect()
        self.movementDirection = MovementDirection
        # Обчислення позиції
        self.Position = (Coordinates[0] * ColliderRect[0], Coordinates[1] * ColliderRect[1])
        self.ColliderRect.x = self.Position[0]
        self.ColliderRect.y = self.Position[1]

