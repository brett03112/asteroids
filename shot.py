import pygame
from circleshape import *
from constants import *

SHOT_RADIUS = 5


class Shot(CircleShape):
    """Represents a shot fired by the player.

    Args:
        CircleShape -- Inherits from CircleShape class.
    Methods:
        draw(screen) -- Draws the shot on the given screen.
        update(dt) -- Updates the shot's position based on its velocity and the time delta.
    """
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius)

    def update(self, dt):
        """
        Moves in a straight line at constant speed. On each frame, 
        it should add (self.velocity * dt) to its position (get self.velocity from its parent class, CircleShape).
        """
        self.position += self.velocity * dt