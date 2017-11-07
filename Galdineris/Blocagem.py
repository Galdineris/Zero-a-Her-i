#26/10
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600,700))

pygame.display.set_caption("Hercules")

screen.fill((0,255,0))

green = (255,255,255)

posicao = [250,200]

tora = pygame.image.load("tora.png")
imagerect = tora.get_rect()

pygame.display.update()

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

                screen.blit(tora, imagerect)
                print("esquerda")
                pygame.display.update()
                
            if event.key == pygame.K_RIGHT:
                
                print("direita")
                pygame.display.update()

    pygame.display.flip()



