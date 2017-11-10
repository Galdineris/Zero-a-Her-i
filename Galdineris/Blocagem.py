#26/10
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600,700))

pygame.display.set_caption("Hercules")

screen.fill((0,255,0))

white = (255,255,255)

posicao = [250,200]

hidra = pygame.Rect(200,550,200,100)
hercules1 = pygame.Rect(140,550,50,100)
hercules2 = pygame.Rect(410,550,50,100)

##image.load("hidra.png")
##imagerect = hidra.get_rect()
pygame.draw.rect(screen,white,hidra,3)
pygame.draw.rect(screen, white,hercules1, 3 )
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
                hidra.top -= 10
                screen.fill((0,255,0))
                pygame.draw.rect(screen, white,hercules1,3)
                print("esquerda")
                
            if event.key == pygame.K_RIGHT:
                hidra.top += 10
                screen.fill((0,255,0))
                pygame.draw.rect(screen, white,hercules2,3)
                print("direita")

        pygame.draw.rect(screen, white,hidra,3)
        pygame.display.update()

            
##            if event.key == pygame.K_UP:
##                hidra.top -= 10
##                screen.fill((0,255,0))
##                pygame.draw.rect(screen,white,hidra,3)
##                print("direita")
##                pygame.display.update()
##                
##            if event.key == pygame.K_DOWN:
##                hidra.top += 10
##                screen.fill((0,255,0))
##                pygame.draw.rect(screen,white,hidra,3)
##                print("direita")
##                pygame.display.update()



pygame.display.flip()



