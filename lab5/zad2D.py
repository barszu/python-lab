import pygame

WINDOW_SIZES = (800, 600)

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (128,128,0)] #red, green, blue
background_color = (0, 0, 0)




class CyclicIterator:
    def __init__(self, items):
        self.items = items
        self.index = 0

    def next(self):
        self.index = (self.index + 1) % len(self.items)
        return self.current()

    def current(self):
        return self.items[self.index]

    def reset(self):
        self.index = 0

class ClickablePolygon:
    def __init__(self, points, colors_collection, screen = None, border_color = (0, 0, 0), border_width = 0):
        self.points = points  # 1st point is the representative one
        self._colors_iterator = CyclicIterator(colors_collection)
        self.color = self._colors_iterator.current()
        self.border_color = border_color
        self.border_width = border_width

        self.mask = None
        self.surface = None
        self.screen = screen

        self.update_surface()

    def draw(self, surface = None):
        """
        This method is responsible for drawing the polygon on the surface.

        It uses the pygame.draw.polygon function to draw the polygon with the current color and points.
        The color is an RGB tuple with an additional alpha value (255) for full opacity.

        Args:
            self: The instance of the ClickablePolygon class.

        Returns:
            None
        """
        if surface is None: surface = self.surface

        pygame.draw.polygon(surface, self.color + (255,), self.points)
        pygame.draw.polygon(surface, self.border_color, self.points, self.border_width) #border only

    def update_surface(self):
        """
        This method is responsible for updating the surface of the polygon.

        It first creates a new surface with the same size as the screen and with support for per-pixel alpha (transparency).
        Then it draws the polygon on this surface using the draw method.
        Finally, it creates a mask from the surface. This mask can be used for efficient collision detection.

        Args:
            self: The instance of the ClickablePolygon class.

        Returns:
            None
        """
        self.surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
        self.draw()
        self.mask = pygame.mask.from_surface(self.surface)

    def change_color(self):
        print("zmieniam kolor!")
        self.color = self._colors_iterator.next()
        self.update_surface()



import math

def get_pyramid_triangle(measures, size, levels_no):
    # (width, height) = measures
    base_center = (measures[0] // 2, measures[1] // 2 - 100)
    level_order = [[] for _ in range(levels_no)] #triangle points
    is_vertex_down = [[] for _ in range(levels_no)]
    level_order_centers = [[] for _ in range(levels_no)] #center of each triangle

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
                level_order[level].append(get_triangle_points((center_x, center_y), size))
                level_order_centers[level].append((center_x, center_y))
                is_vertex_down[level].append(False)

            if level > 0 and i%2 == 1:
                level_order[level].append(get_triangle_points((center_x, center_y - height/3), size, triangle_type="down"))
                level_order_centers[level].append((center_x, center_y - height/3))
                is_vertex_down[level].append(True)

            center_x += size/2
            # center_x = center_x - size / 2
            # center_y = center_y - height / 3

    return level_order, is_vertex_down, level_order_centers


# polygons = [
#     ClickablePolygon([(100, 100), (150, 50), (200, 100)], colors),
#     ClickablePolygon([(300, 300), (350, 250), (400, 300)], colors),
#     ClickablePolygon([(500, 100), (550, 50), (600, 100)], colors)
# ]

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZES)

all_polygons = []
all_is_down = []

a,b,c = get_pyramid_triangle(WINDOW_SIZES, 100, 4)

for level, is_down, centers_level in zip(a, b, c):
    all_is_down.extend(is_down)
    for triangle, center in zip(level, centers_level): #triangle, center
        all_polygons.append(ClickablePolygon(triangle, colors, screen=screen, border_color=(0, 0, 0), border_width=10))




def on_screen_clicked(polygons, mouse_pos): #trzeba graff zrobic
    for i, polygon in enumerate(polygons):
        x, y = mouse_pos
        if polygon.mask.get_at((x, y)):
            polygon.change_color()
            if i == 0: polygon.change_color()
            else: #jest w srodku
                polygons[i-1].change_color()
                polygons[i+1].change_color()
                if all_is_down[i]: #jest do gory nogami
                    parent_idx = (i-1)//3
                    polygons[parent_idx].change_color()
                else: #jest normalnie
                    middle_idx = 3*i + 2
                    polygons[middle_idx].change_color() if middle_idx < len(polygons) else None


            return polygon
    return None


running = True
while running:

    screen.fill(background_color)
    for polygon in all_polygons:
        polygon.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            on_screen_clicked(all_polygons, event.pos)

    pygame.display.flip()

pygame.quit()
