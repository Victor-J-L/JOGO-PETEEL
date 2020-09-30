# Teste Jogo Plataforma Victor
# Pygame Template - Esqueleto para projetos em pygame
import pygame
import random
WIDTH = 360
HEIGHT = 480
FPS = 30

# CORES
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Teste victor Pygame")
clock = pygame.time.Clock()

# GAME LOOP
running = True
while running:

    clock.tick(FPS)
    # Process Input (events)
    for event in pygame.event.get():
       #check for closing the window
       if event.type == pygame.QUIT:
           running = False
    # Update

    # Draw / Render
    screen.fill(BLACK)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()