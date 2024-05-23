import sys
import os

#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import pygame
import Classes
import world

# Ініціалізація Pygame для тестів
pygame.init()
pygame.display.set_mode((800, 600))

# Фікстура для ініціалізації гравця
@pytest.fixture
def player():
    return Classes.Player((7, 9), "Images\\PacMan.jpg", (50, 50))

# Фікстура для ініціалізації ворога
@pytest.fixture
def enemy():
    return Classes.Enemy((7, 9), "Images\\red_ghost.png", (50, 50))

# Тест ініціалізації гравця
def test_player_initialization(player):
    assert player.Position == (350, 450)

# Тест ініціалізації ворога
def test_enemy_initialization(enemy):
    assert enemy.Position == (350, 450)

# Тест руху гравця
def test_player_movement(player):
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
@pytest.fixture
def food():
    return Classes.Food((7, 9), "Images\\food.png", (50, 50))

def test_player_food_collection(player, food):
    player.MovementDirection = (0, 0)
    player.Move()
    assert is_player_center_in_point_center(player.ColliderRect, food.ColliderRect)  # Перевіряємо, що гравець зіткнувся з їжею
    player = Classes.Player((8, 9), "Images\\PacMan.jpg", (50, 50))
    player.MovementDirection = (0, 0)
    player.Move()
    assert not is_player_center_in_point_center(player.ColliderRect, food.ColliderRect)

# Зупинка Pygame після тестів
pygame.quit()

def is_player_center_in_point_center(player_rect, point_rect, tolerance=2):
    # Отримуємо координати центрів обох прямокутників
    player_center_x = player_rect.centerx
    player_center_y = player_rect.centery
    point_center_x = point_rect.centerx
    point_center_y = point_rect.centery

    # Перевіряємо, чи координати центрів збігаються
    if abs(player_center_x - point_center_x) <= tolerance and abs(player_center_y - point_center_y) <= tolerance:
        player_rect.center = point_rect.center
        return True
    else:
        return False
