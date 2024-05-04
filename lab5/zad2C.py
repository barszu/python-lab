# import pygame
# import sys
#
# pygame.init()
# screen = pygame.display.set_mode((800, 600))
#
# # Definiowanie punktów wielokąta
# polygon_points = [(400, 300), (500, 400), (400, 500), (300, 400)]
#
# # Rysowanie wielokąta
# def draw_polygon():
#     pygame.draw.polygon(screen, (255, 0, 0), polygon_points)
#
# # Tworzenie powierzchni dla maski
# polygon_surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
# pygame.draw.polygon(polygon_surface, (255, 0, 0, 255), polygon_points)
#
# # Tworzenie maski z powierzchni
# polygon_mask = pygame.mask.from_surface(polygon_surface)
#
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             # Pobieranie pozycji myszy
#             x, y = event.pos
#             # Sprawdzenie, czy kliknięto wewnątrz maski wielokąta
#             if polygon_mask.get_at((x, y)):
#                 print("Kliknięto wewnątrz wielokąta!")
#
#     screen.fill((0, 0, 0))  # Czyszczenie ekranu
#     draw_polygon()
#     pygame.display.flip()
#
# pygame.quit()

# import pygame
# import sys
#
# pygame.init()
# screen = pygame.display.set_mode((800, 600))
#
# class ClickablePolygon:
#     def __init__(self, points, color):
#         self.points = points
#         self.color = color
#         self.surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
#         pygame.draw.polygon(self.surface, color + (255,), points)
#         self.mask = pygame.mask.from_surface(self.surface)
#
#     def draw(self, surface):
#         pygame.draw.polygon(surface, self.color, self.points)
#
# # Definicja wielokątów
# polygons = [
#     ClickablePolygon([(100, 100), (150, 50), (200, 100)], (255, 0, 0)),
#     ClickablePolygon([(300, 300), (350, 250), (400, 300)], (0, 255, 0)),
#     ClickablePolygon([(500, 100), (550, 50), (600, 100)], (0, 0, 255))
# ]
#
# def check_click(polygons, mouse_pos):
#     for polygon in polygons:
#         x, y = mouse_pos
#         # Sprawdzamy, czy kliknięcie było wewnątrz maski
#         if polygon.mask.get_at((x, y)):
#             print(f"Kliknięto w wielokąt o kolorze {polygon.color}")
#             return polygon
#     return None
#
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             clicked_polygon = check_click(polygons, event.pos)
#             if clicked_polygon:
#                 # Można dodać dodatkowe działania po kliknięciu na konkretny wielokąt
#                 print("Dodatkowa akcja po kliknięciu.")
#
#     screen.fill((0, 0, 0))  # Czyszczenie ekranu
#     for polygon in polygons:
#         polygon.draw(screen)
#     pygame.display.flip()
#
# pygame.quit()


import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

class ClickablePolygon:
    def __init__(self, points, color):
        self.points = points
        self.color = color
        self.clicked = False
        self.update_surface()

    def update_surface(self):
        self.surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
        pygame.draw.polygon(self.surface, self.color + (255,), self.points)
        self.mask = pygame.mask.from_surface(self.surface)

    def draw(self, surface):
        pygame.draw.polygon(surface, self.color, self.points)

    def click(self):
        if not self.clicked:
            self.color = (0, 255, 0)
        else:
            self.color = (255, 0, 0)
        self.clicked = not self.clicked
        self.update_surface()

def check_click(polygons, mouse_pos):
    for polygon in polygons:
        x, y = mouse_pos
        if polygon.mask.get_at((x, y)):
            polygon.change_color()
            print(f"Kliknięto w wielokąt o kolorze {polygon.color}")
            return polygon
    return None

polygons = [
    ClickablePolygon([(100, 100), (150, 50), (200, 100)], (255, 0, 0)),
    ClickablePolygon([(300, 300), (350, 250), (400, 300)], (0, 255, 0)),
    ClickablePolygon([(500, 100), (550, 50), (600, 100)], (0, 0, 255))
]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            check_click(polygons, event.pos)

    screen.fill((0, 0, 0))  # Czyszczenie ekranu
    for polygon in polygons:
        polygon.draw(screen)
    pygame.display.flip()

pygame.quit()


