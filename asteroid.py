import pygame
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    """Represents an asteroid in the game.

    Args:
        CircleShape -- Inherits from CircleShape class.
    Methods:
        draw(screen) -- Draws the asteroid on the given screen.
        update(dt) -- Updates the asteroid's position based on its velocity and the time delta.
    """
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
    def update(self, dt):
        """
        moves in a straight line at constant speed. On each frame, 
        it should add (self.velocity * dt) to its position (get self.velocity from its parent class, CircleShape).
        """
        self.position += self.velocity * dt
