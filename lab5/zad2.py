# import pygame
# import sys
# import time
#
# pygame.init()
# width, height = 800, 600
# screen = pygame.display.set_mode((width, height))
#
# def draw_triangle(screen, points, color):
#     pygame.draw.polygon(screen, color, points)
#
#
# def point_inside_triangle(px, py, points):
#     x1, y1 = points[0]
#     x2, y2 = points[1]
#     x3, y3 = points[2]
#
#     def sign(p1, p2, p3):
#         return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])
#
#     b1 = sign((px, py), (x1, y1), (x2, y2)) < 0.0
#     b2 = sign((px, py), (x2, y2), (x3, y3)) < 0.0
#     b3 = sign((px, py), (x3, y3), (x1, y1)) < 0.0
#
#     return b1 == b2 == b3
#
#
# triangle_points = [(100, 100), (200, 50), (300, 150)]
#
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             mouse_x, mouse_y = pygame.mouse.get_pos()
#             if point_inside_triangle(mouse_x, mouse_y, triangle_points):
#                 print("Trójkąt został kliknięty!")
#
#     screen.fill((0, 0, 0))  # Czyszczenie ekranu, ustawienie na czarno
#     draw_triangle(screen, triangle_points, (255, 0, 0))
#     pygame.display.flip()
#
# pygame.quit()

import pygame
import sys
import math

def draw_equilateral_triangle(screen, center, size, color):
    height = math.sqrt(3)/2 * size
    x, y = center
    points = [
        (x, y - 2/3 * height),  # Wierzchołek na górze
        (x + size/2, y + 1/3 * height),  # Prawy dolny wierzchołek
        (x - size/2, y + 1/3 * height)   # Lewy dolny wierzchołek
    ]
    pygame.draw.polygon(screen, color, points)


def draw_pyramid(screen, base_center, size, levels, base_color, fill_color):
    height = math.sqrt(3)/2 * size
    for level in range(levels):
        for i in range(level + 1):
            center_x = base_center[0] + (i - level/2) * size
            center_y = base_center[1] + level * height
            draw_equilateral_triangle(screen, (center_x, center_y), size, base_color)

            if level != 0:
                # Dodajemy trójkąty "do góry nogami" między trójkątami bieżącego poziomu
                fill_center_x = center_x - size/2
                fill_center_y = center_y - height/2
                draw_equilateral_triangle_upside_down(screen, (fill_center_x, fill_center_y), size, fill_color)

def draw_equilateral_triangle_upside_down(screen, center, size, color):
    height = math.sqrt(3)/2 * size
    x, y = center
    points = [
        (x, y + 2/3 * height),  # Wierzchołek na dole
        (x + size/2, y - 1/3 * height),  # Prawy górny wierzchołek
        (x - size/2, y - 1/3 * height)   # Lewy górny wierzchołek
    ]
    pygame.draw.polygon(screen, color, points)


pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Czyszczenie ekranu, ustawienie na czarno
    draw_pyramid(screen, (width // 2, height // 2 - 100), 50, 4, (255, 255, 0), (0, 255, 0))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

pygame.quit()

