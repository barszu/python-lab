import pygame

class ClickablePolygon:
    def __init__(self, vertices, colors_collection, screen, border_color = (0, 0, 0), border_width = 0):
        """
        This class represents a polygon that can be clicked on.
        :param vertices:
        :param colors_collection: supports next() , current() methods
        :param screen:
        :param border_color:
        :param border_width:
        """
        self.vertices = vertices  # 1st point is the representative one

        self.colors_collection = colors_collection
        self.curr_color = self.colors_collection.current()
        self.border_color = border_color
        self.border_width = border_width

        self.mask = None
        self.surface = None
        self.screen = screen

        self.update_surface(screen)

    def draw(self, surface = None):
        """
        This method is responsible for drawing the polygon on the surface.

        It uses the pygame.draw.polygon function to draw the polygon with the current color and points.
        The color is an RGB tuple with an additional alpha value (255) for full opacity.

        Args:
            self: The instance of the ClickablePolygon class.
            surface: The surface on which the polygon should be drawn.

        Returns:
            None
        """
        if surface is None: surface = self.surface

        pygame.draw.polygon(surface, self.curr_color, self.vertices)
        if self.border_width > 0:
            pygame.draw.polygon(surface, self.border_color, self.vertices, self.border_width) #border only

    def update_surface(self, screen=None):
        """
        This method is responsible for updating the surface of the polygon.

        It first creates a new surface with the same size as the screen and with support for per-pixel alpha (transparency).
        Then it draws the polygon on this surface using the draw method.
        Finally, it creates a mask from the surface. This mask can be used for efficient collision detection.

        Args:
            self: The instance of the ClickablePolygon class.

        Returns:
            None
            :param screen:
        """
        if screen is None:
            screen = self.screen
        self.surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
        self.draw()
        self.mask = pygame.mask.from_surface(self.surface)

    def change_color(self, screen=None):
        # print("zmieniam kolor!")
        if screen is None:
            screen = self.screen
        self.curr_color = self.colors_collection.next()
        self.update_surface(screen)


class ClickableTriangle(ClickablePolygon):
    def __init__(self, vertices, colors_collection, screen, border_color = (0, 0, 0), border_width = 0, center_point=None):
        self.center_point = center_point #center of the triangle label only
        super().__init__(vertices, colors_collection, screen, border_color, border_width)
        assert len(vertices) == 3, "Triangle must have 3 vertices"



############################################################################################################


