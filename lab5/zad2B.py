import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))

# Definicja koloru i pozycji prostokąta
color = (255, 0, 0)  # Czerwony
x, y = 300, 200
width, height = 100, 50

# Tworzenie prostokąta
rect = pygame.Rect(x, y, width, height)

def draw_object():
    pygame.draw.rect(screen, color, rect)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Sprawdź, czy kliknięcie myszą było wewnątrz prostokąta
            if rect.collidepoint(event.pos):
                print("Kliknięto wewnątrz prostokąta!")

    screen.fill((0, 0, 0))  # Czyszczenie ekranu
    draw_object()
    pygame.display.flip()

pygame.quit()

