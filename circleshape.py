import pygame

PLAYER_RADIUS = 20

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        """
        Initializes a CircleShape object with the given x, y, and radius
        arguments. If the object has a containers attribute, it will be
        passed to the Sprite __init__ method. Otherwise, the Sprite __init__
        method will be called with no arguments.
        """
        if hasattr(self, "containers"):
            super().__init__(self.containers) # type: ignore
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        """
        Draws the object onto the given screen.
        Sub-classes must override this method.
        """
        pass

    def update(self, dt):
        # sub-classes must override
        """
        Updates the object's state based on the given time delta.
        Sub-classes must override this method.
        """
        pass