import pygame
from pygame.sprite import Sprite
from random import randint
class Stars(Sprite):
    """A class to manage stars."""

    def __init__(self, ai_game):
        """Initialize the star and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load("./Projects/code/star.bmp")
        self.rect = self.image.get_rect()
        
        self.rect.x = randint(0, self.screen.get_rect().width - self.rect.width)
        self.rect.y = randint(0, self.screen.get_rect().height - self.rect.height)
        

        self.x = float(self.rect.x)
    


