import Classes
import world
import pygame
import sys

# Initialize Pygame
pygame.init()
objects = []
# Set up display
WIDTH, HEIGHT = world.worldWidth*50, (world.worldLenght+1)*50
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Template")
world.setWorld()
world.setFood()
world.SetMotionPoints()
Player = Classes.Player((1,1), "Images\\PacMan.jpg", (50,50))


# Ініціалізація шрифту
pygame.font.init()  # Ініціалізуємо модуль шрифтів Pygame
font = pygame.font.SysFont(None, 36)  # Вибираємо стандартний шрифт

# Ініціалізація UI
ui = Classes.UI(font, "images\\heart.jpg")


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game loop
clock = pygame.time.Clock()
is_running = True


# Завантаження зображення "finish"
finish_image = pygame.image.load("images\\finish.jpg")
finish_image = pygame.transform.scale(finish_image, (WIDTH, HEIGHT))  # Збільшення розміру до розмірів екрану

# Головний цикл гри
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ui.decrease_health()

    # Оновлення гри
    Player.Movement()
    for food in world.foods:
        if Player.ColliderRect.colliderect(food.ColliderRect):
            world.foods.remove(food)
            ui.update_score(ui.score + 10)

    # Перевірка життів
    if ui.health <= 0:
        # Відображення зображення "finish" на екрані
        screen.blit(finish_image, (0, 0))
        pygame.display.flip()
        # Затримка закриття гри на 10 секунд
        pygame.time.delay(2000)
        is_running = False

    # Відображення гри
    screen.fill(BLACK)
    world.DrawingWorldWalls(screen)
    world.DrawingMovementPoints(screen)
    world.DrawingWorldFood(screen)
    screen.blit(Player.Image, Player.ColliderRect)
    ui.draw(screen)
    pygame.display.flip()

    # Обмеження кадрів на секунду
    clock.tick(60)

# Закриття гри
pygame.quit()
sys.exit()