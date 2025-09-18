# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
    
    """
    Main game loop.
    This function initializes pygame and sets up the display,
    then enters an infinite loop where it continually draws the
    player and updates the display.
    """
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, )
    while True: # Main game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, ("black"))
        player.draw(screen)
        pygame.display.flip()
        
        clock.tick(60)
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
