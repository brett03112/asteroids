import pygame
from circleshape import *
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        """
        Initializes a Player object with the given x and y arguments.
        The Player object is a CircleShape with a radius of PLAYER_RADIUS
        and a rotation of 0.
        """
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        
        # in the player class
    def triangle(self):
        """
        Returns a list of 3 points which form a triangle representing the player's nose.
        The triangle is formed by the player's position and the player's rotation.
        The points are in the order of a, b, c, where a is the point in front of the player,
        b is the point to the left of the player, and c is the point to the right of the player.
        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius # type: ignore
        b = self.position - forward * self.radius - right #type: ignore
        c = self.position - forward * self.radius + right #type:ignore
        return [a, b, c]
    
    def draw(self, screen):
        """
        Draws the player onto the given screen.
        The player is drawn as a white triangle with a thickness of 2.
        The triangle is formed by the player's position and rotation.
        """
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
        
    def update(self, dt):
        """
        Updates the player's rotation based on the state of the a and d keys.

        If the a key is pressed, the player is rotated by -PLAYER_TURN_SPEED * dt.
        If the d key is pressed, the player is rotated by PLAYER_TURN_SPEED * dt.
        """
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

    def rotate(self, dt):
        """
        Rotates the player by PLAYER_TURN_SPEED * dt.
        Returns the new rotation.
        """
        
        self.rotation += PLAYER_TURN_SPEED * dt
        return self.rotation