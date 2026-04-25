import pygame
import math

def main():
    pygame.init()

    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Paint")
    clock = pygame.time.Clock()

    color = (0, 0, 255)
    points = []
    mode = "brush"
    start_pos = None
    radius = 15

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # -------- COLOR --------
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    color = (255, 0, 0)
                elif event.key == pygame.K_g:
                    color = (0, 255, 0)
                elif event.key == pygame.K_b:
                    color = (0, 0, 255)
                elif event.key == pygame.K_y:
                    color = (255, 255, 0)

                # -------- MODES --------
                elif event.key == pygame.K_1:
                    mode = 'brush'
                elif event.key == pygame.K_2:
                    mode = 'rectangle'
                elif event.key == pygame.K_3:
                    mode = 'circle'
                elif event.key == pygame.K_4:
                    mode = 'eraser'

                # -------- NEW SHAPES --------
                elif event.key == pygame.K_5:
                    mode = 'square'
                elif event.key == pygame.K_6:
                    mode = 'right_triangle'
                elif event.key == pygame.K_7:
                    mode = 'equilateral_triangle'
                elif event.key == pygame.K_8:
                    mode = 'rhombus'

            # -------- MOUSE DOWN --------
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    start_pos = event.pos

            # -------- MOUSE UP --------
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and start_pos:
                    end_pos = event.pos

                    # RECTANGLE
                    if mode == 'rectangle':
                        rect = pygame.Rect(
                            start_pos,
                            (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])
                        )
                        pygame.draw.rect(screen, color, rect, 2)

                    # CIRCLE
                    elif mode == 'circle':
                        dx = end_pos[0] - start_pos[0]
                        dy = end_pos[1] - start_pos[1]
                        radius_circle = int((dx**2 + dy**2) ** 0.5)
                        pygame.draw.circle(screen, color, start_pos, radius_circle, 2)

                    # -------- SQUARE --------
                    elif mode == 'square':
                        size = min(abs(end_pos[0]-start_pos[0]), abs(end_pos[1]-start_pos[1]))
                        rect = pygame.Rect(start_pos, (size, size))
                        pygame.draw.rect(screen, color, rect, 2)

                    # -------- RIGHT TRIANGLE --------
                    elif mode == 'right_triangle':
                        x1, y1 = start_pos
                        x2, y2 = end_pos

                        points_triangle = [
                            (x1, y1),
                            (x2, y1),
                            (x1, y2)
                        ]
                        pygame.draw.polygon(screen, color, points_triangle, 2)

                    # -------- EQUILATERAL TRIANGLE --------
                    elif mode == 'equilateral_triangle':
                        x1, y1 = start_pos
                        x2, y2 = end_pos

                        base = x2 - x1
                        height = int(abs(base) * (3 ** 0.5) / 2)

                        points_triangle = [
                            (x1, y1),
                            (x2, y1),
                            (x1 + base // 2, y1 - height)
                        ]
                        pygame.draw.polygon(screen, color, points_triangle, 2)

                    # -------- RHOMBUS --------
                    elif mode == 'rhombus':
                        x1, y1 = start_pos
                        x2, y2 = end_pos

                        cx = (x1 + x2) // 2
                        cy = (y1 + y2) // 2

                        points_rhombus = [
                            (cx, y1),
                            (x2, cy),
                            (cx, y2),
                            (x1, cy)
                        ]
                        pygame.draw.polygon(screen, color, points_rhombus, 2)

                    start_pos = None

            # -------- BRUSH / ERASER --------
            if event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:
                    if mode == 'brush':
                        points.append(event.pos)
                        points = points[-256:]

                    elif mode == 'eraser':
                        pygame.draw.circle(screen, (0, 0, 0), event.pos, 20)

        # -------- DRAW BRUSH --------
        if mode == 'brush':
            for i in range(len(points) - 1):
                drawLineBetween(screen, points[i], points[i + 1], radius, color)

        pygame.display.flip()
        clock.tick(60)


# -------- LINE DRAW --------
def drawLineBetween(screen, start, end, width, color):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = i / iterations
        x = int(start[0] + (end[0] - start[0]) * progress)
        y = int(start[1] + (end[1] - start[1]) * progress)
        pygame.draw.circle(screen, color, (x, y), width)


main()