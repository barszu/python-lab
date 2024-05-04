import pygame

class GameEngineCreator:
    """
    A class used to represent a Game Engine Creator.

    ...

    Attributes
    ----------
    polygons : list
        a list of polygons in the game
    screen : pygame.Surface
        the screen on which the game is displayed
    background_color : tuple
        the color of the background in RGB format
    after_click_function : function
        the function to be executed after a click event

    Methods
    -------
    find_polygon(mouse_pos):
        Returns the polygon at the given mouse position.
    on_screen_clicked(mouse_pos, later_do_function):
        Executes a function when a polygon is clicked on the screen.
    run():
        Starts the game loop.
    """

    def find_polygon(self, mouse_pos):
        """
        Returns the polygon at the given mouse position.

        Parameters
        ----------
        mouse_pos : tuple
            the position of the mouse

        Returns
        -------
        Polygon
            the polygon at the given mouse position
        """
        for p in self.polygons:
            x, y = mouse_pos
            if p.mask.get_at((x, y)):
                return p
        return None

    def __init__(self, polygons = [], screen = None, background_color = (255, 255, 255), after_click_function = None):
        """
        Constructs all the necessary attributes for the Game Engine Creator object.

        Parameters
        ----------
        polygons : list
            a list of polygons in the game
        screen : pygame.Surface
            the screen on which the game is displayed
        background_color : tuple
            the color of the background in RGB format
        after_click_function : function
            the function to be executed after a click event
        """
        self.polygons = polygons
        self.screen = screen
        self.background_color = background_color
        self.after_click_function = after_click_function

    def on_screen_clicked(self, mouse_pos, later_do_function= None):
        """
        Executes a function when a polygon is clicked on the screen.

        Parameters
        ----------
        mouse_pos : tuple
            the position of the mouse
        later_do_function : function
            the function to be executed after a click event

        Returns
        -------
        Polygon
            the clicked polygon
        """
        clicked_polygon = self.find_polygon(mouse_pos)
        if clicked_polygon is not None:
            if later_do_function is not None:
                later_do_function(clicked_polygon)
            else:
                clicked_polygon.change_color()
            return clicked_polygon

        return None

    def run(self):
        """
        Starts the game loop.
        """
        running = True
        while running:
            self.screen.fill(self.background_color)
            for polygon in self.polygons:
                polygon.draw(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.on_screen_clicked(event.pos, self.after_click_function)

            pygame.display.flip()




