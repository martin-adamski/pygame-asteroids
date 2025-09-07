import pygame
import sys
from constants import *
from player import *
from asteroids import * 
from asteroidfields import *
from shot import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    shot_grp = pygame.sprite.Group()
    asteroids_grp = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Shot.containers = (shot_grp, updatable, drawable)
    Asteroid.containers = (asteroids_grp, updatable, drawable)
    AsteroidField.containers = (updatable)

    player_obj = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroidfield_obj = AsteroidField()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill('black')

        updatable.update(dt)

        for asteroid in asteroids_grp:
            if asteroid.collision(player_obj):
                print("Game Over!")
                sys.exit()

        for asteroid in asteroids_grp:
            for bullet in shot_grp:
                if asteroid.collision(bullet):
                    asteroid.split()
                    bullet.kill()

        for ply in drawable:
            ply.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
