import pygame
import datetime
import math

WIDTH, HEIGHT = 800, 800
CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2 - 22 
CORRECTION_ANGLE = 0 

RED = (220, 20, 60)
BLACK = (10, 10, 10)
WHITE = (255, 255, 255)

SEC_HAND_LEN = 200
MIN_HAND_LEN = 180

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")
clock = pygame.time.Clock()

try:
    dial_img = pygame.image.load("images/clock.png").convert_alpha()
    dial_img = pygame.transform.scale(dial_img, (750, 750))
    dial_rect = dial_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))
except:
    dial_img = pygame.Surface((WIDTH, HEIGHT))
    dial_rect = dial_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))

def draw_hand(surf, color, length, width, angle):
    rad_angle = math.radians(angle - 90 + CORRECTION_ANGLE)
    end_x = CENTER_X + length * math.cos(rad_angle)
    end_y = CENTER_Y + length * math.sin(rad_angle)
    pygame.draw.line(surf, color, (CENTER_X, CENTER_Y), (end_x, end_y), width)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = datetime.datetime.now()
    
    seconds = now.second + now.microsecond / 1000000.0
    minutes = now.minute + seconds / 60.0

    sec_angle = seconds * 6
    min_angle = minutes * 6

    screen.fill(WHITE)
    screen.blit(dial_img, dial_rect)

    pygame.draw.circle(screen, BLACK, (CENTER_X, CENTER_Y), 10)
    
    draw_hand(screen, BLACK, MIN_HAND_LEN, 7, min_angle)
    draw_hand(screen, RED, SEC_HAND_LEN, 2, sec_angle)
    
    pygame.draw.circle(screen, RED, (CENTER_X, CENTER_Y), 4)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()