import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteoidfield import *

def main():
    # Welcome message in terminal
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Initialise pygame
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Add sprite groups and add objects to groups
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (drawable, updatable)
    Asteroid.containers = (drawable, updatable, asteroids)
    AsteroidField.containers = (updatable)

    
    # Initialise player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()

    # Main game loop
    while True:

        # Enable pygames close button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Set background to black    
        screen.fill((0,0,0))

        # iterate through the updateable group and update each object
        for each in updatable:
            each.update(dt)
        # iterate through the drawable group and update each object
        for item in drawable:
            item.draw(screen)

        # reset the display
        pygame.display.flip()
        
        # limit fps to 60 but dont allow slowdown if fps dips
        MAX_DT = 0.05
        dt = min(clock.tick(60) / 1000, MAX_DT)

if __name__ == "__main__":
    main()