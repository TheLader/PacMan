import pytest
import pygame
import Classes
import world

# Ініціалізація Pygame для тестів
pygame.init()
pygame.display.set_mode((800, 600))

# Тест ініціалізації гравця
def test_player_initialization():
    player = Classes.Player((7, 9), "Images\\PacMan.jpg", (50, 50))
    assert player.Position == (350, 450)

# Тест ініціалізації ворогів
def test_enemy_initialization():
    enemy = Classes.Enemy((8, 5), "Images\\red_ghost.png", (50, 50))
    assert enemy.Position == (400, 250)

# Тест руху гравця
def test_player_movement():
    player = Classes.Player((7, 9), "Images\\PacMan.jpg", (50, 50))
    player.MovementDirection = (1, 0)
    player.Move()
    assert player.Position == (353, 450)

# Тест зіткнення гравця з ворогом
def test_player_enemy_collision():
    player = Classes.Player((8, 9), "Images\\PacMan.jpg", (50, 50))
    enemy = Classes.Enemy((7, 9), "Images\\red_ghost.png", (50, 50))
    player.Move()
    enemy.Move()
    assert not enemy.ColliderRect.colliderect(player.ColliderRect)  # Перевіряємо, що немає зіткнення
    player = Classes.Player((7, 9), "Images\\PacMan.jpg", (50, 50))
    player.Move()
    assert enemy.ColliderRect.colliderect(player.ColliderRect)


# Тест збору їжі гравцем
def test_player_food_collection():
    player = Classes.Player((7, 9), "Images\\PacMan.jpg", (50, 50))
    food = Classes.Food((7, 9), "images\\food.png", (50, 50))
    player.MovementDirection = (0,0)
    player.Move()
    assert is_player_center_in_point_center(player.ColliderRect, food.ColliderRect)  # Перевіряємо, що гравець зіткнувся з їжею
    player = Classes.Player((8, 9), "Images\\PacMan.jpg", (50, 50))
    player.MovementDirection = (0, 0)
    player.Move()
    assert not is_player_center_in_point_center(player.ColliderRect, food.ColliderRect)


# Зупинка Pygame після тестів
pygame.quit()

# Якщо потрібно, можна додати більше тестів для інших функцій та сценаріїв вашої гри.
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
