import pygame


class Ball:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = self.screen.get_size()

        self.radius = 25
        self.x = self.width // 2
        self.y = self.height // 2

        self.color = (255, 0, 0)

    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy

        if self.radius <= new_x <= self.width - self.radius:
            self.x = new_x

        if self.radius <= new_y <= self.height - self.radius:
            self.y = new_y

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)