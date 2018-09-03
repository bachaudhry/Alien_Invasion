import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    """Initialize game, settings and screen object."""

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship and pass ai_settings as an argument.
    ship = Ship(ai_settings, screen)

    # Start the main loop for the game.
    while True:
        # Imports game functions and events
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)


run_game()

