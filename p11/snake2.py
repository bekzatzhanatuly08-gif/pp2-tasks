import pygame
import random

# Initialize Pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

# ---------------- SNAKE ----------------
dx, dy = 1, 0
snake = [(5, 5)]

# ---------------- GAME STATE ----------------
speed = 5
score = 0
level = 1

# ---------------- FOOD SYSTEM ----------------
# food теперь хранит тип + время жизни
food = None

food_types = {
    "red": 3,     # редкая → больше очков
    "green": 1,   # обычная
    "blue": 5     # редкая → много очков
}

FOOD_LIFETIME = 5000  # 5 секунд (в миллисекундах)

# ---------------- FOOD GENERATOR ----------------
def gen_food():
    """Создаёт еду в случайной позиции, не внутри змеи"""
    while True:
        x = random.randint(0, (WIDTH // BLOCK_SIZE) - 1)
        y = random.randint(0, (HEIGHT // BLOCK_SIZE) - 1)

        if (x, y) not in snake:
            food_type = random.choice(list(food_types.keys()))

            return {
                "pos": (x, y),
                "type": food_type,
                "time": pygame.time.get_ticks()
            }

food = gen_food()

run = True

# ================= MAIN LOOP =================
while run:

    # -------- INPUT --------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            # запрет разворота
            if event.key == pygame.K_DOWN and dy == 0:
                dx, dy = 0, 1
            elif event.key == pygame.K_UP and dy == 0:
                dx, dy = 0, -1
            elif event.key == pygame.K_RIGHT and dx == 0:
                dx, dy = 1, 0
            elif event.key == pygame.K_LEFT and dx == 0:
                dx, dy = -1, 0

    # -------- MOVE SNAKE --------
    head = snake[0]
    new_head = (head[0] + dx, head[1] + dy)

    # -------- COLLISION WALL --------
    x, y = new_head
    if x < 0 or x >= WIDTH // BLOCK_SIZE or y < 0 or y >= HEIGHT // BLOCK_SIZE:
        run = False

    # -------- SELF COLLISION --------
    if new_head in snake:
        run = False

    if not run:
        break

    snake.insert(0, new_head)

    # -------- FOOD TIMER (исчезновение еды) --------
    current_time = pygame.time.get_ticks()

    if current_time - food["time"] > FOOD_LIFETIME:
        food = gen_food()

    # -------- EATING FOOD --------
    if new_head == food["pos"]:

        # добавляем очки по типу еды
        score += food_types[food["type"]]

        # рост змейки
        snake.append(snake[-1])

        # новая еда
        food = gen_food()

        # уровень и скорость
        if score % 3 == 0:
            level += 1
            speed += 1

    else:
        snake.pop()

    # -------- DRAWING --------
    screen.fill(BLACK)

    # food color by type
    fx, fy = food["pos"]

    if food["type"] == "red":
        color = (255, 0, 0)
    elif food["type"] == "green":
        color = (0, 255, 0)
    else:
        color = (0, 0, 255)

    pygame.draw.rect(
        screen,
        color,
        (fx * BLOCK_SIZE, fy * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
    )

    # snake
    for seg in snake:
        pygame.draw.rect(
            screen,
            GREEN,
            (seg[0] * BLOCK_SIZE, seg[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
        )

    # score + level
    screen.blit(font.render(f"Score: {score}", True, WHITE), (10, 10))
    screen.blit(font.render(f"Level: {level}", True, WHITE), (10, 40))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()