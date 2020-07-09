import pygame
from pygame.sprite import Sprite

class Airplane(Sprite):
    """A class to represent a single airplane in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the airplane image and set its rect attribute.
        self.image = pygame.image.load('images/airplane.bmp')
        self.rect = self.image.get_rect()

        # Start each new airplane near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the airplane's exact horizontal position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if airplane is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the airplane to the right or left."""
        self.x += (self.settings.airplane_speed * self.settings.fleet_direction)
        self.rect.x = self.x