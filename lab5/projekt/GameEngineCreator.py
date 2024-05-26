import time

import pygame
import random
import numpy
import scipy.ndimage

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

    def __init__(self, polygons = [], screen = None, background_color = (255, 255, 255), after_click_function = None, initial_shuffles = 0):
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
        self.initial_shuffles = initial_shuffles

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

    def init_game(self):
        """
        Initializes the game.
        """
        self.screen.fill(self.background_color)
        for polygon in self.polygons:
            polygon.draw(self.screen)
        pygame.display.flip()

    def shuffle_polygons(self, with_animation = False):
        """
        Shuffles the polygons in the game.
        """
        for i in range(self.initial_shuffles):
            polygon = random.choice(self.polygons)
            self.on_screen_clicked(polygon.center_point, self.after_click_function)
            time.sleep(0.01) if with_animation else None

    def run(self):
        """
        Starts the game loop.
        """
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.on_screen_clicked(event.pos, self.after_click_function)
                    if self.check_win():
                        self.display_win_message()
                        pygame.time.wait(5000) # Czekaj 5 sekund
                        running = False


    def check_win(self):
        """
        Checks if the game is won.
        """
        curr_color = self.polygons[0].curr_color
        for polygon in self.polygons:
            if polygon.curr_color != curr_color:
                return False
        return True

    def blur_screen(self):
        """
        Applies a blur effect to the screen.
        """
        # Pobierz tablicę pikseli z ekranu
        pixels = pygame.surfarray.array3d(self.screen)

        # Zastosuj rozmycie gaussowskie
        blurred_pixels = scipy.ndimage.filters.gaussian_filter(pixels, sigma=5)

        # Przekształć rozmyte piksele z powrotem na format zrozumiały dla Pygame
        blurred_pixels = pygame.surfarray.make_surface(blurred_pixels)

        # Wyświetl rozmyte piksele na ekranie
        self.screen.blit(blurred_pixels, (0, 0))

    def display_win_message(self):
        """
        Displays a win message on the screen.
        """
        self.blur_screen()  # Rozmyj ekran
        font = pygame.font.Font(None, 120)  # Ustaw rozmiar czcionki
        text = font.render("Wygrana!", 1, (255, 51, 204))  # Utwórz tekst
        text_pos = text.get_rect(centerx=self.screen.get_width() / 2, centery=self.screen.get_height() / 2)  # Ustaw pozycję tekstu na środku ekranu
        self.screen.blit(text, text_pos)  # Wyświetl tekst na ekranie
        pygame.display.flip()  # Aktualizuj ekran





