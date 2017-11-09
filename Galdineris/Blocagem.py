#26/10
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600,700))

pygame.display.set_caption("Hercules")

screen.fill((0,255,0))

white = (255,255,255)

posicao = [250,200]

tora = pygame.Rect(200,400,200,100)
##image.load("tora.png")
##imagerect = tora.get_rect()
pygame.draw.rect(screen,white,tora,3)
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
                tora.left -= 10
                screen.fill((0,255,0))
                pygame.draw.rect(screen,white,tora,3)
                print("esquerda")
                pygame.display.update()
            if event.key == pygame.K_RIGHT:
                tora.right += 10
                screen.fill((0,255,0))
                pygame.draw.rect(screen,white,tora,3)
                print("direita")
                pygame.display.update()

                
##            if event.key == pygame.K_UP:
##                tora.top -= 10
##                screen.fill((0,255,0))
##                pygame.draw.rect(screen,white,tora,3)
##                print("direita")
##                pygame.display.update()
##                
##            if event.key == pygame.K_DOWN:
##                tora.top += 10
##                screen.fill((0,255,0))
##                pygame.draw.rect(screen,white,tora,3)
##                print("direita")
##                pygame.display.update()


    pygame.display.flip()



