import pygame
import random
import os

pygame.init()

# ------------------- SETUP -------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

car_img = pygame.image.load(os.path.join(BASE_DIR, "resources", "player.png"))
road_img = pygame.image.load(os.path.join(BASE_DIR, "resources", "road.png"))
coin_img = pygame.image.load(os.path.join(BASE_DIR, "resources", "coin.png"))
coin2_img = pygame.image.load(os.path.join(BASE_DIR, "resources", "coin_2.png"))
coin3_img = pygame.image.load(os.path.join(BASE_DIR, "resources", "coin_3.png"))
enemy_img = pygame.image.load(os.path.join(BASE_DIR, "resources", "enemy.png"))

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

# ------------------- SCALE -------------------
car_img = pygame.transform.scale(car_img, (50, 120))
coin_img = pygame.transform.scale(coin_img, (40, 40))
coin2_img = pygame.transform.scale(coin2_img, (40, 40))
coin3_img = pygame.transform.scale(coin3_img, (40, 40))
enemy_img = pygame.transform.scale(enemy_img, (50, 100))
road_img = pygame.transform.scale(road_img, (WIDTH, HEIGHT))

# ------------------- MAP COINS -------------------
coin_data = {
    "yellow": (coin_img, 1),
    "blue": (coin2_img, 3),
    "red": (coin3_img, 5)
}

# ------------------- PLAYER -------------------
car_x = WIDTH // 2 - 25
car_y = HEIGHT - 130
car_speed = 5

# ------------------- OBJECTS -------------------
coins = []
enemies = []

coin_speed = 4
enemy_speed = 4

# ------------------- SCORE -------------------
score = 0
font = pygame.font.SysFont(None, 36)

clock = pygame.time.Clock()
running = True

# ------------------- GAME LOOP -------------------
while running:
    screen.blit(road_img, (0, 0))

    # -------- EVENTS --------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # -------- PLAYER MOVE --------
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH - 50:
        car_x += car_speed

    # -------- SPAWN COINS --------
    if random.randint(1, 40) == 1:
        coin_type = random.choice(list(coin_data.keys()))

        coins.append({
            "x": random.randint(0, WIDTH - 40),
            "y": -40,
            "type": coin_type
        })

    # -------- SPAWN ENEMIES --------
    if random.randint(1, 90) == 1:
        enemies.append({
            "x": random.randint(0, WIDTH - 50),
            "y": -100
        })

    # -------- MOVE OBJECTS --------
    for coin in coins:
        coin["y"] += coin_speed

    for enemy in enemies:
        enemy["y"] += enemy_speed

    # -------- PLAYER RECT --------
    car_rect = pygame.Rect(car_x, car_y, 30, 85)

    # -------- COIN COLLISION --------
    new_coins = []

    for coin in coins:
        img, value = coin_data[coin["type"]]

        coin_rect = pygame.Rect(coin["x"], coin["y"], 40, 40)

        if car_rect.colliderect(coin_rect):
            score += value
        else:
            new_coins.append(coin)

    coins = new_coins

    # -------- ENEMY COLLISION --------
    for enemy in enemies:
        enemy_rect = pygame.Rect(enemy["x"], enemy["y"], 40, 100)

        if car_rect.colliderect(enemy_rect):
            running = False

    # -------- CLEAN UP --------
    coins = [c for c in coins if c["y"] < HEIGHT]
    enemies = [e for e in enemies if e["y"] < HEIGHT]

    # -------- SPEED SCALING --------
    enemy_speed = 4 + score // 10

    # -------- DRAW COINS --------
    for coin in coins:
        img, _ = coin_data[coin["type"]]
        screen.blit(img, (coin["x"], coin["y"]))

    # -------- DRAW ENEMIES --------
    for enemy in enemies:
        screen.blit(enemy_img, (enemy["x"], enemy["y"]))

    # -------- DRAW PLAYER --------
    screen.blit(car_img, (car_x, car_y))

    # -------- SCORE --------
    text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()