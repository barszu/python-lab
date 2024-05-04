import pygame
import time
import random

N = 4 # Number of rows and columns
COLORS_NO = 2
CELL_SIZE = 100

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
colors = [red, green, blue, yellow] #0 1 2 3

board_colors_ids = [[0 for _ in range(N)] for _ in range(N)]

def draw_square(screen, x, y, color):
    pygame.draw.rect(screen, color, (x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE-1, CELL_SIZE-1)) #1 px margin

def change_color(x,y):
    board_colors_ids[x][y] = (board_colors_ids[x][y] + 1) % COLORS_NO
    draw_square(window, x, y, colors[board_colors_ids[x][y]])

def change_neighbours_and_this_color(x, y, rerender=False):
    for (dx, dy) in [(0,0), (0,1), (0,-1), (1,0), (-1,0)]: #this, neighbours
        nx = (x + dx) % N
        ny = (y + dy) % N
        change_color(nx, ny)
    if rerender: pygame.display.update()


def init_board():
    # aka shuffle on board | can be reversed by player
    for _ in range(50):
        change_neighbours_and_this_color(random.randint(0, N-1), random.randint(0, N-1))
    pygame.display.update()

pygame.init()
window = pygame.display.set_mode((N*CELL_SIZE, N*CELL_SIZE))
pygame.display.set_caption("My Game")
window.fill((0, 0, 0)) #black

init_board()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            x = x // CELL_SIZE
            y = y // CELL_SIZE
            change_neighbours_and_this_color(x, y, rerender=True)




# draw_square(window, 0, 0, red)
# pygame.display.update()

# time.sleep(3)

# zrob to samo z trojkatami! <- praca doomwea

# sasiedzi -> graf
# odzyskanie ktory i jaki to lista schodkowa el => 1 3 5 7 ...



