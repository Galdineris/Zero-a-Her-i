#26/10
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600,400))

pygame.display.set_caption("Hercules")

screen.fill((0,255,0))

pygame
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_LEFT:
                print("esquerda")
                
            if event.key == pygame.K_RIGHT:
                print("direita")
    pygame.display.flip()



