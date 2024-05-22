import numpy as np
import Classes
import world

import pygame
import sys

# Initialize Pygame
pygame.init()
objects = []
# Set up display
WIDTH, HEIGHT = world.worldWidth * 50, (world.worldLenght + 1) * 50
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Template")
world.setWorld()
world.setFood()
world.SetMotionPoints()
Player = Classes.Player((7, 9), "Images\\PacMan.jpg", (50, 50))
Enemy1 = Classes.Enemy((8, 5), "Images\\red_ghost.png", (50, 50))
Enemy2 = Classes.Enemy((9, 5), "Images\\green_ghost.png", (50, 50))
Enemy3 = Classes.Enemy((10, 5), "Images\\blue_ghost.png", (50, 50))
Enemy4 = Classes.Enemy((11, 5), "Images\\purple_ghost.png", (50, 50))
Enemys = [Enemy1, Enemy2, Enemy3, Enemy4]
# Ініціалізація шрифту
pygame.font.init()  # Ініціалізуємо модуль шрифтів Pygame
font = pygame.font.SysFont(None, 36)  # Вибираємо стандартний шрифт

# Ініціалізація UI
ui = Classes.UI(font, "images\\heart.jpg")

arrow = pygame.image.load("images\\arrow.png")
arrow = pygame.transform.scale(arrow, (100, 100))
arrow.get_rect().update(10,10,10,10)
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game loop
clock = pygame.time.Clock()
is_running = True
InMainMenu = True

# Завантаження зображення "finish"
finish_image = pygame.image.load("images\\finish.jpg")
finish_image = pygame.transform.scale(finish_image, (WIDTH, HEIGHT))  # Збільшення розміру до розмірів екрану

# Завантаження зображення "finish"
winner_image = pygame.image.load("Images/winner.jpg")
winner_image = pygame.transform.scale(winner_image, (WIDTH, HEIGHT))  # Збільшення розміру до

# Головний цикл гри
while is_running:
    if InMainMenu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    InMainMenu = False
                    ui.health = 3
                    Player = Classes.Player((7, 9), "Images\\PacMan.jpg", (50, 50))
                    Enemy1 = Classes.Enemy((8, 5), "Images\\red_ghost.png", (50, 50))
                    Enemy2 = Classes.Enemy((9, 5), "Images\\green_ghost.png", (50, 50))
                    Enemy3 = Classes.Enemy((10, 5), "Images\\blue_ghost.png", (50, 50))
                    Enemy4 = Classes.Enemy((11, 5), "Images\\purple_ghost.png", (50, 50))
                    Enemys = [Enemy1, Enemy2, Enemy3, Enemy4]
                    world.foods = []
                    world.setFood()
                    ui.score = 0

        screen.fill(WHITE)
        screen.blit(arrow, arrow.get_clip())
        print(arrow.get_rect())
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ui.decrease_health()


        def is_player_center_in_point_center(player_rect, point_rect, tolerance=2):
            # Отримуємо координати центрів обох прямокутників
            player_center_x = player_rect.centerx
            player_center_y = player_rect.centery
            point_center_x = point_rect.centerx
            point_center_y = point_rect.centery

            # Перевіряємо, чи координати центрів збігаються
            if abs(player_center_x - point_center_x) <= tolerance and abs(
                    player_center_y - point_center_y) <= tolerance:
                player_rect.center = point_rect.center
                return True
            else:
                return False


        # Функція для перевірки чи може піти гравець в цьому напрямку
        def CanMove(Player, point):
            if Player.MovementDirection == (1, 0) and point.movementDirection[1] != 1:
                return False
            elif Player.MovementDirection == (-1, 0) and point.movementDirection[3] != 1:
                return False
            elif Player.MovementDirection == (0, -1) and point.movementDirection[0] != 1:
                return False
            elif Player.MovementDirection == (0, 1) and point.movementDirection[2] != 1:
                return False
            else:
                return True


        # Update
        # Умови для перевірки чи може гравець розвернутися на 180 градусів
        if (Player.MovementDirection[0] == Player.NextMovementDirection[0] * -1 and Player.MovementDirection[0] != 0):
            Player.MovementDirection = Player.NextMovementDirection
            Player.NextMovementDirection = (0, 0)
            Player.ChangeAngel(Player.MovementDirection)
        if (Player.MovementDirection[1] == Player.NextMovementDirection[1] * -1 and Player.MovementDirection[1] != 0):
            Player.MovementDirection = Player.NextMovementDirection
            Player.NextMovementDirection = (0, 0)
            Player.ChangeAngel(Player.MovementDirection)
        for food in world.foods:
            if is_player_center_in_point_center(Player.ColliderRect, food.ColliderRect):
                world.foods.remove(food)
                ui.update_score(ui.score + 10)  # Оновлюємо рахунок на 10 очок
        for point in world.motionPoints:
            # перевіряє чи знаходиться центр гравця в центрі точки руху
            if is_player_center_in_point_center(Player.ColliderRect, point.ColliderRect):
                PreviousDirection = Player.MovementDirection
                Player.MovementDirection = Player.NextMovementDirection
                if not CanMove(Player, point):
                    Player.MovementDirection = PreviousDirection
                Player.ChangeAngel(Player.MovementDirection)
                if Player.MovementDirection == (1, 0) and point.movementDirection[1] != 1:
                    Player.MovementDirection = (0, 0)
                if Player.MovementDirection == (-1, 0) and point.movementDirection[3] != 1:
                    Player.MovementDirection = (0, 0)
                if Player.MovementDirection == (0, -1) and point.movementDirection[0] != 1:
                    Player.MovementDirection = (0, 0)
                if Player.MovementDirection == (0, 1) and point.movementDirection[2] != 1:
                    Player.MovementDirection = (0, 0)

        Player.Movement()
        # Player.Image = pygame.transform.rotate(Player.Image, 45)
        # Перевірка життів
        if ui.health <= 0:
            # Відображення зображення "finish" на екрані
            screen.blit(finish_image, (0, 0))
            pygame.display.flip()
            # Затримка закриття гри на 10 секунд
            pygame.time.delay(1000)
            InMainMenu = True

        if ui.score == 980:
            screen.blit(winner_image, (0, 0))
            pygame.display.flip()
            # Затримка закриття гри на 10 секунд
            pygame.time.delay(3000)
            is_running = False

        for enemy in Enemys:
            if (enemy.ColliderRect.colliderect(Player.ColliderRect)):
                ui.decrease_health()
                Player = Classes.Player((7, 9), "Images\\PacMan.jpg", (50, 50))
            enemy.StupidMovement()

        # Draw
        screen.fill(BLACK)
        world.DrawingWorldWalls(screen)
        world.DrawingMovementPoints(screen)
        world.DrawingWorldFood(screen)

        # screen.blit(wall.Image, wall.Position)
        screen.blit(Player.Image, Player.ColliderRect)
        screen.blit(Enemy1.Image, Enemy1.ColliderRect)
        screen.blit(Enemy2.Image, Enemy2.ColliderRect)
        screen.blit(Enemy3.Image, Enemy3.ColliderRect)
        screen.blit(Enemy4.Image, Enemy4.ColliderRect)

        # Оновлення та відображення інтерфейсу
        ui.draw(screen)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)


# Quit Pygame
pygame.quit()
sys.exit()
