import pygame

#
windowWidth = 600
windowHeight = 800
gridSize = 30
grid = (10, 20)

class Player(self):
  

def main():
  window = pygame.display.set_mode((windowWidth, windowHeight))
  pygame.display.set_caption('Wind of change')
  mainLoop = True
  clock = pygame.time.Clock()

  while mainLoop:
    # FPS
    clock.tick(60)

    # Get input


    # Update


    # Draw
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        mainLoop = False
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          mainLoop = False

    pygame.draw.rect(window, (255, 0, 0), (10, 10, 580, 780), 5, 10)
    pygame.display.flip()

  pygame.quit()
# end of main function


main()
