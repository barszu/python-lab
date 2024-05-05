import pygame
from LinkedListsCollections import CyclicList
from Shapes import ClickableTriangle
from Options import window_sizes, background_color, colours, shuffle_moves_no
from GameEngineCreator import GameEngineCreator
import math

def get_pyramid_triangles(measures, size, levels_no):
    # (width, height) = measures
    # returns [(traingle_points, centers, is_vertex_down)]
    base_center = (measures[0] // 2, measures[1] // 2 - 100)
    res = []

    def get_triangle_points(center, size, triangle_type = "up"):
        _height = math.sqrt(3)/2 * size
        x, y = center
        if triangle_type == "up":
            return [
                (x, y - 2/3 * _height),  # Wierzchołek na górze
                (x + size/2, y + 1/3 * _height),  # Prawy dolny wierzchołek
                (x - size/2, y + 1/3 * _height)   # Lewy dolny wierzchołek
            ]
        elif triangle_type == "down":
            return [
                (x - size / 2, y - 1 / 3 * height),  # Lewy górny wierzchołek
                (x + size / 2, y - 1 / 3 * height),  # Prawy górny wierzchołek
                (x, y + 2 / 3 * height),  # Wierzchołek na dole
            ]


    height = math.sqrt(3)/2 * size
    for level in range(levels_no):
        center_x = base_center[0] - (level/2) * size
        center_y = base_center[1] + level * height
        for i in range(0, 2*level + 1): # O 012 01234 ...

            if i%2 == 0:
                res.append((get_triangle_points((center_x, center_y), size), (center_x, center_y), False))

            if level > 0 and i%2 == 1:
                res.append((get_triangle_points((center_x, center_y - height/3), size, triangle_type="down"), (center_x, center_y - height/3), True))

            center_x += size/2

    return res




def main():
    pyramid_level = 4
    triangle_side_size = 100
    triangle_border_width = 10

    pygame.init()
    screen = pygame.display.set_mode(window_sizes)

    all_polygons = []
    for triangle, center, is_down in get_pyramid_triangles(window_sizes, triangle_side_size, pyramid_level):
        all_polygons.append(
            ClickableTriangle(triangle, CyclicList(colours), screen=screen, border_color=(0, 0, 0), border_width=triangle_border_width, center_point=center)
        )

    game_engine = GameEngineCreator(all_polygons, screen, background_color, after_click_function=None, initial_shuffles=shuffle_moves_no)
    def handle_click(clicked_triangle):
        (x, y) = clicked_triangle.center_point
        # print(f"Kliknięto w trójkąt o środku w punkcie ({x}, {y})")
        r = triangle_side_size / math.sqrt(3) - triangle_border_width
        for dx, dy in [(-r, 0), (r, 0), (0, -r), (0, r)]:
            new_x = x + dx
            new_y = y + dy
            neighbour_triangle = game_engine.find_polygon((new_x, new_y))
            if neighbour_triangle is not None:
                neighbour_triangle.change_color()

    game_engine.after_click_function = handle_click
    game_engine.init_game()
    game_engine.shuffle_polygons()
    game_engine.run()

    pygame.quit()


if __name__ == "__main__":
    main()