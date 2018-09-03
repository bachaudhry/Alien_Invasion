class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 750
        self.bg_color = (255, 255, 255)

        # Ship settings.
        self.ship_speed_factor = 1.5