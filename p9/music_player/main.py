import pygame
import sys
from player import MusicPlayer

pygame.init()

screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption("Music Player")

font = pygame.font.SysFont("Arial", 24)

player = MusicPlayer("music")

clock = pygame.time.Clock()

running = True

while running:
    screen.fill((30, 30, 30))

    track_text = font.render(f"Track: {player.get_current_track()}", True, (255, 255, 255))
    pos_text = font.render(f"Time: {player.get_position()} sec", True, (200, 200, 200))
    help_text = font.render("P-Play S-Stop N-Next B-Back Q-Quit", True, (100, 255, 100))

    screen.blit(track_text, (50, 80))
    screen.blit(pos_text, (50, 120))
    screen.blit(help_text, (50, 200))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()
            elif event.key == pygame.K_s:
                player.stop()
            elif event.key == pygame.K_n:
                player.next_track()
            elif event.key == pygame.K_b:
                player.prev_track()
            elif event.key == pygame.K_q:
                running = False

    clock.tick(30)

pygame.quit()
sys.exit()