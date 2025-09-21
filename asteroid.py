import random
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

    def split(self):
            """
            Splits the asteroid into two smaller asteroids when hit by a shot.
            If the asteroid is too small, it is destroyed.
            Otherwise, it is split into two smaller asteroids with random velocities.
            """
            self.kill()
            if self.radius <= ASTEROID_MIN_RADIUS:
                return
            else:
                angle = random.uniform(20, 50)
                new_radius = self.radius - ASTEROID_MIN_RADIUS
                velocity1 = self.velocity.rotate(angle)
                velocity2 = self.velocity.rotate(-angle)
                asteroid1 = Asteroid(self.position.x, self.position.y, new_radius) # type: ignore
                asteroid2 = Asteroid(self.position.x, self.position.y, new_radius) # type: ignore
                asteroid1.velocity = velocity1 * 1.2
                asteroid2.velocity = velocity2 * 1.2