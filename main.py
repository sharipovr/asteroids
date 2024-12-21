import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
  pygame.get_init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()
  Player.containers = (updatable, drawable)
  Asteroid.containers = (asteroids, updatable, drawable)
  Shot.containers = (shots, updatable, drawable)
  AsteroidField.containers = (updatable)
  
  x = SCREEN_WIDTH / 2
  y = SCREEN_HEIGHT / 2
  player = Player(x, y)
  asteroid_field = AsteroidField();
  
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return

    for obj in updatable:
      obj.update(dt)
    
    for obj in asteroids:
      if obj.check_collission(player) == True:
        print("Game over!")
        sys.exit()
      for shot in shots:
        if obj.check_collission(shot) == True:
          obj.kill()
          shot.kill()

    screen.fill(color="black")

    for obj in drawable:
      obj.draw(screen)
    
    for obj in shots:
      obj.draw(screen)

    pygame.display.flip()
    passed = clock.tick(60.0)
    dt = passed / 1000

if __name__ == "__main__":
  main()

