#26/10
import pygame
import time
import sys

def draw_tela():
    screen.fill((0,255,0))
    pygame.draw.rect(screen,white,hidra1,3)
    pygame.draw.rect(screen,white,hidra2,3)
    pygame.draw.rect(screen,white,hidra3,3)
    pygame.draw.rect(screen,white,hidra4,3)
    pygame.draw.rect(screen,white,hercules,3)
    pygame.draw.rect(screen,white,galho,2)
    pygame.display.update()


pygame.init()

screen = pygame.display.set_mode((600,700))

pygame.display.set_caption("Hercules")

screen.fill((0,255,0))

white = (255,255,255)

posicao = [250,200]

hidra1 = pygame.Rect(200,550,200,100)
hidra2 = pygame.Rect(200,450,200,100)
hidra3 = pygame.Rect(200,350,200,100)
hidra4 = pygame.Rect(200,250,200,100)
galho = pygame.Rect(140,450,50,100)
hercules = pygame.Rect(140,550,100,50)

##image.load("hidra.png")
##imagerect = hidra.get_rect()
draw_tela()

tecla = 1
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
                hercules = pygame.Rect(140,550,50,100)
                for i in range(20):
                    hidra1.top += 5
                    draw_tela()
                print("esquerda")  
                
                
            if event.key == pygame.K_RIGHT:
                hercules = pygame.Rect(410,550,50,100)
                for i in range(20):
                    hidra1.top -= 5
                    draw_tela() 
                print("direita")
                    

        draw_tela()

            
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



