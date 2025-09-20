# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    
    """
    Main game loop.
    This function initializes pygame and sets up the display,
    then enters an infinite loop where it continually draws the
    player and updates the display.
    """
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Create sprite groups first
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Assign the sprite groups to the Player, Asteroid and AsteroidField classes
    Player.containers = (updatable, drawable) # type: ignore
    Asteroid.containers = (updatable, drawable, asteroids) # type: ignore
    AsteroidField.containers = (updatable, ) # type: ignore
    
    # Create objects after containers are assigned
    asteroid_field = AsteroidField()
    
    # Create a clock to manage the frame rate
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, )
    while True: # Main game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, ("black"))
        
        # Draw all drawable objects individually
        for sprite in drawable:
            sprite.draw(screen)
        
        pygame.display.flip()
        
        # Update all updatable objects individually
        for sprite in updatable:
            sprite.update(dt)
        
        # Limit to 60 frames per second
        # dt is the time since the last frame in seconds
        # dt is used to make movement smooth and consistent
        # regardless of the frame rate
        # dt is passed to the player's update method
        # to ensure the player rotates at the same speed
        # regardless of the frame rate
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
