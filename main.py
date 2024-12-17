import pygame
from constants import *

def main():
  pygame.get_init()
  print("Starting asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  clock = pygame.time.Clock()
  dt = 0

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    screen.fill(color="black")
    pygame.display.flip()
    passed = clock.tick(60.0)
    dt = passed / 1000

if __name__ == "__main__":
  main()

