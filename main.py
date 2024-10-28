import pygame
import pygame.freetype
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteoidfield import *
from shot import *


def main():
    # Welcome message in terminal
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Initialise pygame
    pygame.init()
    GAME_FONT = pygame.freetype.SysFont('Comic Sans MS', 30)
    GAME_OVER_FONT = pygame.freetype.SysFont('Comic Sans MS', 100)
    savefile = "saves.txt"
    try:
        with open(savefile, "r") as h_s:
            high_score = h_s.read()
    except FileNotFoundError:
        with open(savefile, "w") as new:
            new.write("0")
        high_score = "0"
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Add sprite groups and add objects to groups
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (drawable, updatable)
    Asteroid.containers = (drawable, updatable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (drawable, updatable, shots)

    
    # Initialise player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()
    score = 0
    game_over = False

    # Main game loop
    while True:

        # Enable pygames close button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Set background to black    
        screen.fill((0,0,0))
        if game_over == False:
            GAME_FONT.render_to(screen, (40, 40), f"High Score: {high_score}", (255, 255, 255))
            GAME_FONT.render_to(screen, (40, 80), f"Score: {score}", (255, 255, 255))
        # iterate through the updateable group and update each object
        for each in updatable:
            each.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                print(score)
                if score > int(high_score):
                    with open(savefile, "w") as outfile:
                        outfile.write(str(score))
               
                game_over = True
                break
            
        for shot in shots:
            for asteroid in asteroids:
                if shot.collision(asteroid):
                    asteroid.split()
                    shot.kill()
                    score += 1

        # iterate through the drawable group and update each object
        for item in drawable:
            item.draw(screen)

        # reduce shot cooldown timer
        player.timer  -= dt



        if game_over:
            for asteroid in asteroids:
                asteroid.kill()
            player.kill()
            GAME_OVER_FONT.render_to(screen, (320, 250), "Game Over!", (255, 255, 255))
            GAME_OVER_FONT.render_to(screen, (320, 350), f"High Score: {high_score}", (255, 255, 255))
            GAME_OVER_FONT.render_to(screen, (320, 450), f"Score: {score}", (255, 255, 255))
        
        # reset the display
        pygame.display.flip()

        # limit fps to 60 but dont allow slowdown if fps dips
        MAX_DT = 0.05
        dt = min(clock.tick(60) / 1000, MAX_DT)

if __name__ == "__main__":
    main()